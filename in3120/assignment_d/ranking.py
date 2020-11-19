#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from corpus import Corpus
from invertedindex import Posting, InvertedIndex
import math
from collections import Counter, defaultdict
from normalization import BrainDeadNormalizer
from tokenization import BrainDeadTokenizer


class Ranker(ABC):
    """
    Abstract base class for rankers used together with document-at-a-time traversal.
    """

    @abstractmethod
    def reset(self, document_id: int) -> None:
        """
        Resets the ranker, i.e., prepares it for evaluating another document.
        """
        pass

    @abstractmethod
    def update(self, term: str, multiplicity: int, posting: Posting) -> None:
        """
        Tells the ranker to update its internals based on information from one
        query term and the associated posting. This method might be invoked multiple
        times if the query contains multiple unique terms. Since a query term might
        occur multiple times in a query, the query term's multiplicity or occurrence
        count in the query is also provided.
        """
        pass

    @abstractmethod
    def evaluate(self) -> float:
        """
        Returns the current document's relevancy score. I.e., evaluates how relevant
        the current document is, given all the previous update invocations.
        """
        pass


class BrainDeadRanker(Ranker):
    """
    A dead simple ranker.
    """

    def __init__(self):
        self._score = 0.0

    def reset(self, document_id: int) -> None:
        self._score = 0.0

    def update(self, term: str, multiplicity: int, posting: Posting) -> None:
        self._score += multiplicity * posting.term_frequency

    def evaluate(self) -> float:
        return self._score


class BetterRanker(Ranker):
    """
    A ranker that does traditional TF-IDF ranking, possibly combining it with
    a static document score (if present).

    The static document score is assumed accessible in a document field named
    "static_quality_score". If the field is missing or doesn't have a value, a
    default value of 0.0 is assumed for the static document score.
    """

    def __init__(self, corpus: Corpus, inverted_index: InvertedIndex, mode=1):
        self._mode = mode #  1 for cosine similarity, 0 for TF-IDF
        self._score = 0.0
        self._document_id = None
        self._corpus = corpus
        self._inverted_index = inverted_index
        self._dynamic_score_weight = 1.0  # TODO: Make this configurable.
        self._static_score_weight = 1.0  # TODO: Make this configurable.
        self._static_score_field_name = "static_quality_score"  # TODO: Make this configurable.
        self._document_vector = Counter()
        self._query_vector = defaultdict(lambda: defaultdict(float))
        self._normalizer = BrainDeadNormalizer()
        self._tokenizer = BrainDeadTokenizer()

    def _build_document_vector(self):
        doc = self._corpus.get_document(self._document_id).get_field('body', None)
        doc = self._normalizer.normalize(doc)
        doc = self._tokenizer.tokens(doc)
        self._document_vector = Counter([token[0] for token in doc])

    def _to_tfidf_normalize(self, vector):
        #  Update vector with TF-IDF
        for token, freq in vector.items():
            tf_score = 1 + math.log(freq) if freq > 0 else 0
            idf_score = math.log(self._corpus.size() / self._inverted_index.get_document_frequency(token))
            vector[token] = tf_score * idf_score

        #  Normalize vector
        norm = math.sqrt(sum(val**2 for val in vector.values()))
        for token, freq in vector.items():
            vector[token] = vector[token]/norm

    def _cosine_similarity(self, vector_1, vector_2):
        keys_1 = set(vector_1.keys())
        keys_2 = set(vector_2.keys())
        intersection = keys_1 & keys_2
        return sum(vector_1[key] * vector_2[key] for key in intersection)

    def reset(self, document_id: int) -> None:
        self._score = 0.0
        self._document_id = document_id
        self._document_vector = Counter()
        self._query_vector = defaultdict(lambda: defaultdict(float))
        if self._mode == 1:
            self._build_document_vector()
            self._to_tfidf_normalize(self._document_vector)

    def update(self, term: str, multiplicity: int, posting: Posting) -> None:
        if self._mode == 1:
            #  Build up query vector
            self._query_vector[term] = multiplicity
        else:
            tf_score = 1 + math.log(posting.term_frequency) if posting.term_frequency > 0 else 0
            idf_score = math.log(self._corpus.size() / self._inverted_index.get_document_frequency(term))
            self._score += multiplicity * tf_score * idf_score

    def evaluate(self) -> float:
        document = self._corpus[self._document_id]
        static_quality_score = float(document[self._static_score_field_name] or 0.0)
        if self._mode == 1:
            self._to_tfidf_normalize(self._query_vector)
            self._score = self._cosine_similarity(self._query_vector, self._document_vector)

        return static_quality_score + self._score

    """
    I implemented ranker based on TF-IDF and cosine similarity. Cosine similarity vectorizes only the body
    field of each document. Values in vectors are TF-IDF score.
    Subjectively, the results with cosine similarity ranking tend to give higher score to the documents with
    higher frequency of terms that are more rare in the collection. As the result, some documents that
    do not actually include all the search terms can rank higher, which is not desirable (as I understand) in the
    current search engine, since we would like to give more credit to the documents that contain all the search terms.
    """


