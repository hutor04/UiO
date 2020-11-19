from nltk.probability import ConditionalFreqDist, ConditionalProbDist, MLEProbDist
from itertools import chain
from typing import Iterable, List, Tuple
import sys
import time
from multiprocessing import Pool, cpu_count
from sklearn.metrics import accuracy_score

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
        self.states_index = None  # The list of possible states in HMM
        self.len_states = None  # The amount of states in HMM

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
        trellis = [[] * self.len_states for _ in range(len_observations)]
        # List of (Viterbi, (Previous State, Current State))

        # Initialization
        trellis[0] = [(self.transition[START_TAG].logprob(state) + self.emission[state].logprob(sentence[0]), (0, s))
                      for s, state in enumerate(self.states_index)]

        # Main Loop
        for t in range(1, len_observations):
            for s, state in enumerate(self.states_index):
                max_i, max_v = max_argmax((trellis[t - 1][i][0] + self.transition[state1].logprob(state)
                                           for i, state1 in enumerate(self.states_index)))

                trellis[t].append((max_v + self.emission[state].logprob(sentence[t]), (max_i, s)))

        # Restore Path
        last = max(trellis[-1], key=lambda x: x[0])
        path = []
        path.insert(0, last[1][1])
        prev = last[1][0]

        for i in range(len(trellis) - 2, -1, -1):
            path.insert(0, trellis[i][prev][1][1])
            prev = trellis[i][prev][1][0]

        return [self.states_index[i] for i in path]

    def transform(self, sentences: List[List[str]]) -> List[List[str]]:
        print('Making predictions...')
        labels = []
        total = len(sentences)
        start = time.time()
        chunksize = int(total/100) if int(total/10) > 0 else 1
        cores = cpu_count()

        # Use this code if multiprocessing fails
        """
        for i, sentence in enumerate(sentences):
            labels.append(self._viterbi(sentence))
            index = i + 1
            progress = ((i + 1) / total * 100)
            time_elapsed = time.time() - start
            sys.stdout.write('\r{} of {} {:.2f}% sentences processed | Time: {:.2f}'.format(index, total, progress,
                                                                                                time_elapsed))
            sys.stdout.flush()
        
        """

        #"""
        with Pool(cores) as pool:
            for i, label_sequence in enumerate(pool.imap(self._viterbi, sentences, chunksize=chunksize)):
                labels.append(label_sequence)
                index = i + 1
                progress = ((i + 1) / total * 100)
                time_elapsed = time.time() - start
                sys.stdout.write('\r{} of {} {:.2f}% sentences processed | Time: {:.2f}'.format(index, total, progress,
                                                                                                time_elapsed))
                sys.stdout.flush()

        #"""

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
    sent_d, tags_d = read_dataset(DEV_DATA)

    tagger = PosTagger()
    tagger.fit(sent, tags)

    print(">>>Trained on TRAIN_DATA, Predicting TRAIN_DATA:")
    predict = tagger.transform(sent)

    acc = accuracy(tags, predict)

    print('')
    print('Accuracy: {}'.format(acc))

    print(">>>Trained on TRAIN_DATA, Predicting DEV_DATA::")
    predict = tagger.transform(sent_d)

    acc = accuracy(tags_d, predict)

    print('')
    print('Accuracy: {}'.format(acc))
