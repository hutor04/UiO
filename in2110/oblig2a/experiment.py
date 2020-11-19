from nltk.probability import ConditionalFreqDist, ConditionalProbDist, MLEProbDist
from itertools import chain
from typing import Iterable, List, Tuple
import sys
import time

TRAIN_DATA = "no_bokmaal-ud-train.tt"
DEV_DATA = "no_bokmaal-ud-dev.tt"
START_TAG = '<s>'


def read_dataset(filename: str) -> Tuple[List[List[str]], List[List[str]]]:
    print('Reading data...')

    sentences = []
    labels = []

    with open(filename, 'r') as input_file:
        sentence_tokens = []
        sentence_labels = []

        for line in input_file:
            split_line = line.split('\t')

            if len(split_line) == 1:
                sentences.append(sentence_tokens)
                sentence_tokens = []

                labels.append(sentence_labels)
                sentence_labels = []

            else:
                sentence_tokens.append(split_line[0].strip())
                sentence_labels.append(split_line[1].strip())

    return sentences, labels


def bigrams(sequence: List[str]) -> List[Tuple[str, str]]:

    sequence = [START_TAG] + sequence
    bgs = [(sequence[i], sequence[i + 1]) for i in range(len(sequence) - 1)]

    return bgs


def max_argmax(data: Iterable) -> int:
    return max(enumerate(data), key=lambda x: x[1])


class SmoothProbDist(MLEProbDist):
    def prob(self, key):
        value = super().prob(key)

        return value if value != 0 else 1e-20


class PosTagger(object):
    def __init__(self):
        self.transition = None
        self.emission = None
        self.states_index = None
        self.len_states = None

    def fit(self, sentences: List[List[str]], labels: List[List[str]]) -> None:
        print('Training model...')

        self.transition = ConditionalFreqDist()
        self.emission = ConditionalFreqDist()

        for sentence, label_seq in zip(sentences, labels):
            for label_bgr in bigrams(label_seq):
                self.transition[label_bgr[0]][label_bgr[1]] += 1

            for token, tag in zip(sentence, label_seq):
                self.emission[tag][token] += 1

        self.transition = ConditionalProbDist(self.transition, MLEProbDist)
        self.emission = ConditionalProbDist(self.emission, SmoothProbDist)

        self.states_index = list(self.emission.keys())
        self.len_states = len(self.states_index)

    def _viterbi(self, sentence: List[str]) -> List[str]:
        len_observations = len(sentence)
        track = [[()] * self.len_states for _ in range(len_observations)]

        for state in range(self.len_states):
            track[0][state] = (self.transition[START_TAG].logprob(self.states_index[state]) +
                               self.emission[self.states_index[state]].logprob(sentence[0]), (0, state))

        # Main Loop
        for t in range(1, len_observations):
            for s in range(self.len_states):
                max_i, max_v = max_argmax((track[t - 1][s1][0] + self.transition[self.states_index[s1]].logprob(self.states_index[s]) +
                              self.emission[self.states_index[s]].logprob(sentence[t]) for s1 in range(self.len_states)))

                track[t][s] = (max_v, (max_i, s))

        # Restore Path
        last = max(track[-1], key=lambda x: x[0])
        path = []
        path.insert(0, last[1][1])
        prev = last[1][0]

        for i in range(len(track) - 2, -1, -1):
            path.insert(0, track[i][prev][1][1])
            prev = track[i][prev][1][0]

        return [self.states_index[i] for i in path]

    def transform(self, sentences: List[List[str]]) -> List[List[str]]:
        print('Making predictions...')
        labels = []
        total = len(sentences)
        start = time.time()

        for i, sentence in enumerate(sentences):
            labels.append(self._viterbi(sentence))  # Viterbi is applied

            sys.stdout.write(f'\r{i + 1} of {total} {(i + 1)/total*100:.2f}% sentences processed | '
                             f'Time: {time.time() - start:.2f}')
            sys.stdout.flush()

        return labels


def accuracy(true: List[List[str]], pred: List[List[str]]) -> float:
    true = chain(*true)
    pred = chain(*pred)

    size = 0
    fails = 0

    for tag, prediction in zip(true, pred):
        if tag != prediction:
            fails += 1
        size += 1

    return 1-fails/size


if __name__ == '__main__':
    sent, tags = read_dataset(TRAIN_DATA)

    tagger = PosTagger()
    tagger.fit(sent, tags)

    #tagger._viterbi(sent[0])
    test_sent = sent[:100]
    test_tags = tags[:100]

    predict = tagger.transform(test_sent)
    acc = accuracy(test_tags, predict)

    print('')
    print(f'Accuracy: {acc:.4f}')
