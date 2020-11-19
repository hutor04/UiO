from collections import defaultdict
from itertools import chain
from math import sqrt
import heapq
import json
from stopwords import stop_words
from typing import Iterable, List, Dict, Tuple, Set, Any

from in2110.oblig1b import visualize_word_vectors
from in2110.corpora import aviskorpus_10_nn

# Settings
TRANSLATION_TABLE = dict.fromkeys(map(ord, '\'«»!"#$%&()*+,/:;<=>?@[\]^_`{|}~@.-'), None)


def preprocess(sentences: Iterable[str]) -> List[List[str]]:
    result = []

    for sentence in sentences:
        clean_sentence = sentence.replace('<s>', '').replace('</s>', '').lower().translate(TRANSLATION_TABLE)
        tokenized_sentence = clean_sentence.split()
        removed_stop_words = [token for token in tokenized_sentence if token not in stop_words]
        result.append(removed_stop_words)

    return result


def context_window(sent: List[str], pos: int, size: int) -> List[str]:
    if pos < 0 or pos > len(sent) - 1:
        raise ValueError('pos argument is out of range')

    prefix = sent[max(0, pos - size):pos]
    suffix = sent[pos + 1:min(len(sent), pos + size + 1)]

    return prefix + suffix


class WordVectorizer(object):
    def __init__(self, max_features: int, window_size: int, normalize=False):
        self.max_features = max_features
        self.window_size = window_size
        self.normalize = normalize
        self.matrix = defaultdict(lambda: defaultdict(float))
        self.is_normalized = False

    def load_from_json(self, filename: str) -> None:
        with open(filename, 'r') as input_file:
            self.matrix = json.load(input_file)

    def write_to_json(self, filename: str) ->None:
        with open(filename, 'w') as output_file:
            dump = json.dumps(self.matrix)
            output_file.write(dump)

    def _n_frequent_types(self, sentences: List[List[str]]) -> Set:
        print('Counting frequences...')
        accumulator = defaultdict(int)

        for sentence in sentences:
            for token in sentence:
                accumulator[token] += 1
        return set(heapq.nlargest(self.max_features, accumulator, key=accumulator.get))

    def fit(self, sentences: List[List[str]]) -> Dict[str, Dict[Any, float]]:
        types_to_use = self._n_frequent_types(sentences)

        print('Building matrix...')

        for sentence in sentences:
            for i in range(len(sentence)):
                if sentence[i] in types_to_use:
                    context = context_window(sentence, i, self.window_size)
                    filtered_context = [token for token in context if token in types_to_use]
                    for token in filtered_context:
                        self.matrix[sentence[i]][token] += 1

        if self.normalize:
            print('Normalizing matrix...')
            self.normalize_vectors()

        return self.matrix

    def transform(self, words: List[str]) -> List[Dict[Any, float]]:
        checked_words = []
        for word in words:
            if word in set(self.matrix.keys()):
                checked_words.append(word)
            else:
                print(f'{word} - IS NOT FOUND IN FEATURES, USE SOMETHING ELSE INSTEAD')

        return [self.matrix[w] for w in checked_words]

    def vector_norm(self, word):
        vector = self.matrix.get(word)

        if vector:
            return sqrt(sum(val**2 for val in vector.values()))
        else:
            raise ValueError('words not found')

    def normalize_vectors(self) -> None:
        for key in self.matrix.keys():
            vector_length = self.vector_norm(key)
            for key2 in self.matrix[key]:
                self.matrix[key][key2] = self.matrix[key][key2] / vector_length

    def _get_vectors(self, w1: str, w2: str) -> Tuple[Any, Any, Set, Set, Set]:
        vector_1 = self.matrix.get(w1)
        vector_2 = self.matrix.get(w2)

        if vector_1 and vector_2:
            keys_1 = set(vector_1.keys())
            keys_2 = set(vector_2.keys())
            intersection = keys_1 & keys_2

            return vector_1, vector_2, keys_1, keys_2, intersection

        else:
            raise ValueError('words not found')

    def euclidean_distance(self, w1: str, w2: str) -> float:
        vector_1, vector_2, keys_1, keys_2, intersection = self._get_vectors(w1, w2)

        intersection_squared_dif = ((vector_1[key] - vector_2[key])**2 for key in intersection)
        vector_1_subset = (vector_1[key]**2 for key in keys_1 - intersection)
        vector_2_subset = (vector_2[key] ** 2 for key in keys_2 - intersection)

        all_items = chain(intersection_squared_dif, vector_1_subset, vector_2_subset)

        distance = sqrt(sum(all_items))

        return distance

    def cosine_similarity(self, w1: str, w2: str) -> float:
        vector_1, vector_2, keys_1, keys_2, intersection = self._get_vectors(w1, w2)

        dot_product = sum(vector_1[key] * vector_2[key] for key in intersection)

        if self.normalize:
            similarity = dot_product
        else:
            similarity = dot_product / (self.vector_norm(w1) * self.vector_norm(w2))

        return similarity

    def nearest_neighbors(self, w: str, k=5, distancetype=1) -> Tuple[str, float]:
        if distancetype == 1:
            all_distances = [(key, self.cosine_similarity(w, key)) for key in self.matrix.keys()]
            return heapq.nlargest(k + 1, all_distances, key=lambda x: x[1])[1:]
        else:
            all_distances = [(key, self.euclidean_distance(w, key)) for key in self.matrix.keys()]
            return heapq.nsmallest(k + 1, all_distances, key=lambda x: x[1])[1:]


if __name__ == '__main__':
    print('Loading texts...')
    sent = list(aviskorpus_10_nn.sentences())

    print('Preprocessing texts...')
    sent = preprocess(sent)

    print('Vectorizer initiated...')
    v = WordVectorizer(10000, 5, normalize=True)

    m = v.fit(sent)

    print('Testing similarity...')
    eucl = v.euclidean_distance('tyskland', 'norge')
    cosine = v.cosine_similarity('tyskland', 'norge')
    print(f'Euclidean distance between Tyskland and Norge is: {eucl}')
    print(f'Cosine similarity between Tyskland and Norge is: {cosine}')

    nn = v.nearest_neighbors('norge', k=5)
    print('The nearest neighbours of Norge are:')

    for term, measure in nn:
        print(f'{term} - {measure}')

    print('Plotting word vectors...')

    visualize_word_vectors(v, ['bergen', 'stavanger', 'trondheim', 'oslo', 'krf', 'frp', 'sv', 'venstre', 'høyre',
                               'senterpartiet', 'forfattaren', 'poeten', 'dikt', 'romanen', 'boka',
                               'rogaland', 'hordaland', 'telemark', 'nordland', 'østfold', 'tyskland', 'usa', 'sveits',
                               'nederland'])
