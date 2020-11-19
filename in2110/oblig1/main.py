from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

import nltk
nltk.data.path.append("/Users/yauhenk/Documents/UiO/in2110/data/nltk_data")
from nltk.stem.snowball import SnowballStemmer

from typing import Iterable, List, Dict, Tuple
from collections import Counter

#from in2110.corpora import norec
from norec import Norec
norec = Norec('norec.zip', 'norec-metadata.json')

#from in2110.oblig1 import scatter_plot
from oblig1 import scatter_plot

#Settings
CATEGORY_FILTER: List[str] = ['games', 'restaurants', 'literature']
MAX_FEATURES: int = 5000
K: int = 10


def prepare_data(documents):
    data = []
    labels = []

    for document in documents:
        if document.metadata['category'] in CATEGORY_FILTER:
            data.append(document.text)
            labels.append(document.metadata['category'])

    return data, labels


def token_type_counter(documents: Iterable[List[str]]) -> (int, int):
    """
    Helper function for Task 1, b). It used for the evaluation of the tokenizers.
    :param documents: iterable of lists of strings where each string represents a document
    :return: total number of tokens and total number of types calculated from the input
    """
    types = set()
    tokens = 0

    for document in documents:
        for token in document:
            types.add(token)
        tokens += len(document)

    return tokens, len(types)


def category_stats(data_in: List[str]) -> Dict[str, Tuple[int, float]]:
    """
    Helper function for Task 1, c). It counts the number of documents per category and calculates the proportion
    of the category within the data set.
    :param data_in: list of strings, each string represents a category of a document in the data set.
    :return: returns the dictionary, where each key is a category, the value is a tuple of category count and its
    proportion.
    """
    counter = Counter(data_in)
    result = {key: (value, value/sum(counter.values())*100) for key, value in counter.items()}

    return result


def _category_stats_printer(data_in: Dict[str, Tuple[int, float]]) -> None:
    for key in data_in.keys():
        print(f'Category: {key}, no documents: {data_in[key][0]}, percentage: {data_in[key][1]:.2f}')


def tokenize(text):
    stemmer = SnowballStemmer('norwegian')
    translation_table = dict.fromkeys(map(ord, '\'«»!"#$%&()*+,/:;<=>?@[\]^_`{|}~@.-'), None)
    text = text.lower().translate(translation_table)
    tokens = nltk.word_tokenize(text)

    return list(map(stemmer.stem, tokens))


class Vectorizer(object):
    def __init__(self):

        self.count_vectorizer = CountVectorizer(lowercase=False, tokenizer=lambda x: x, max_features=MAX_FEATURES)
        self.tfidf = TfidfTransformer()

    def train(self, data):
        vec = self.count_vectorizer.fit_transform(data)
        vec_tfidf = self.tfidf.fit_transform(vec)

        print(len(self.count_vectorizer.get_feature_names()))

        return vec, vec_tfidf

    def vectorize(self, data):
        vec = self.count_vectorizer.transform(data)
        vec_tfidf = self.tfidf.transform(vec)

        return vec, vec_tfidf


def create_knn_classifier(vec, labels, k):

    clf = KNeighborsClassifier(n_neighbors=k)
    clf.fit(vec, labels)

    return clf


if __name__ == '__main__':
    # Prepare Data
    train_data, train_labels = prepare_data(norec.train_set())
    dev_data, dev_labels = prepare_data(norec.dev_set())
    test_data, test_labels = prepare_data(norec.test_set())
    print("Data prepared...\n")

    # Tokenize Data
    train_data_tokens = list(map(tokenize, train_data))
    dev_data_tokens = list(map(tokenize, dev_data))
    test_data_tokens = list(map(tokenize, test_data))
    print("Data tokenized...\n")

    # Print Input Data Statistics
    test_number_tokens, test_number_types = token_type_counter(test_data_tokens)
    print(f'Test data set currently includes {test_number_tokens} tokens and {test_number_types} types..\n')


    train_category_stats = category_stats(train_labels)
    dev_category_stats = category_stats(dev_labels)
    test_category_stats = category_stats(test_labels)
    print(f'Train data set includes categories:')
    _category_stats_printer(train_category_stats)
    print()

    print(f'Development data set includes categories:')
    _category_stats_printer(dev_category_stats)
    print()

    print(f'Test data set includes categories:')
    _category_stats_printer(test_category_stats)
    print()

    # Vectorization
    v = Vectorizer()

    train_vector, train_idf_vector = v.train(train_data_tokens)

    # Plot vectors
    scatter_plot(train_idf_vector, train_labels)
    #scatter_plot(train_vector, train_labels)

    dev_vector, dev_idf_vector = v.vectorize(dev_data_tokens)
    test_vector, test_idf_vector = v.vectorize(test_data_tokens)
    print('Vectors are ready...\n')

    # Classification
    cls = create_knn_classifier(train_idf_vector, train_labels, K)
    dev_predict = cls.predict(dev_idf_vector)
    test_predict = cls.predict(test_idf_vector)
    print('kNN is ready...\n')

    dev_score = accuracy_score(dev_labels, dev_predict)
    test_score = accuracy_score(test_labels, test_predict)

    print(f'Precision:\nDevelopment set: {dev_score:.4f}\nTest set: {test_score:.4f}')
