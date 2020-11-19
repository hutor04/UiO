#!/usr/bin/python
# -*- coding: utf-8 -*-

# import itertools
from collections import Counter
from utilities import Sieve
import heapq
from corpus import Corpus
from tokenization import Tokenizer
from typing import Callable, Any, Iterable
from normalization import Normalizer


class SuffixArray:
    """
    A simple suffix array implementation. Allows us to conduct efficient substring searches.
    The prefix of a suffix is an infix!

    In a serious application we'd make use of least common prefixes (LCPs), pay more attention
    to memory usage, and add more lookup/evaluation features.
    """

    def __init__(self, corpus: Corpus, fields: Iterable[str], normalizer: Normalizer, tokenizer: Tokenizer):
        self._corpus = corpus
        self._normalizer = normalizer
        self._tokenizer = tokenizer
        self._haystack = []
        self._suffixes = []
        self._build_suffix_array(fields)

    def _build_suffix_array(self, fields: Iterable[str]) -> None:
        """
        Builds a simple suffix array from the set of named fields in the document collection.
        The suffix array allows us to search across all named fields in one go.
        """

        delimiter = ' \0 '
        heap = []

        for doc in self._corpus:
            doc_id = doc.get_document_id()
            text = ''

            for field in fields:
                text += self._normalize(doc.get_field(field, None))
                text += delimiter

            self._haystack.append(text)

            token_ranges = self._tokenizer.ranges(text)
            doc_suffixes = [(self._haystack[doc_id][index[0][0]:], doc_id, index[0][0]) for index in (token_ranges[i:]
                            for i in range(len(token_ranges)))]
            heap += doc_suffixes

        # Sorting
        heapq.heapify(heap)
        while len(heap) > 0:
            _, doc_id, index = heapq.heappop(heap)
            self._suffixes.append((doc_id, index))

    def _normalize(self, buffer: str) -> str:
        """
        Produces a normalized version of the given string. Both queries and documents need to be
        identically processed for lookups to succeed.
        """

        # Tokenize and join to be robust to nuances in whitespace and punctuation.
        return self._normalizer.normalize(" ".join(self._tokenizer.strings(self._normalizer.canonicalize(buffer))))

    def evaluate(self, query: str, options: dict, callback: Callable[[dict], Any]) -> None:
        """
        Evaluates the given query, doing a "phrase prefix search".  E.g., for a supplied query phrase like
        "to the be", we return documents that contain phrases like "to the bearnaise", "to the best",
        "to the behemoth", and so on. I.e., we require that the query phrase starts on a token boundary in the
        document, but it doesn't necessarily have to end on one.

        The matching documents are ranked according to how many times the query substring occurs in the document,
        and only the "best" matches are returned to the client via the supplied callback function. Ties are
        resolved arbitrarily.

        The client can supply a dictionary of options that controls this query evaluation process: The maximum
        number of documents to return to the client is controlled via the "hit_count" (int) option.

        The callback function supplied by the client will receive a dictionary having the keys "score" (int) and
        "document" (Document).
        """

        def search(substring: str):
            """
            Binary search, additionally walks to the sides of the match, in order to find multiple matches.
            :param substring: str
            :return: List[Tuple[int, int]]
                    Return a list of tuples (docid, suffix location)
            """
            left = 0
            right = len(self._suffixes) - 1
            res = []

            def _recover_text(suffix) -> str:
                """
                Helper function that gets text fragment from the collection
                :param suffix Tuple[int, int]
                                TextID and suffix location
                :return: str
                             Suffix text
                """
                doc_id, index = suffix
                return self._haystack[doc_id][index:]

            while left <= right:
                mid = int(left + (right - left) / 2)
                _recover_text(self._suffixes[mid])
                doc_suffix = _recover_text(self._suffixes[mid])

                # Match Found
                if doc_suffix.startswith(substring):
                    res.append(self._suffixes[mid])

                    # Walk Left from Match
                    for item in self._suffixes[mid - 1::-1]:
                        doc_suffix = _recover_text(item)
                        if doc_suffix.startswith(substring):
                            res.append(item)
                        else:
                            break

                    # Walk Right from Match
                    for item in self._suffixes[mid + 1:]:
                        doc_suffix = _recover_text(item)
                        if doc_suffix.startswith(substring):
                            res.append(item)
                        else:
                            break

                    return res

                # Trying other sides
                elif doc_suffix < substring:
                    left = mid + 1

                else:
                    right = mid - 1

            return -1

        normalized_query = self._normalize(query)
        results = search(normalized_query)  # (docID, padding)

        if results != -1 and query != '':
            counter = Counter([x for x, y in results])  # (key: docID: value: frequency)
            sieve = Sieve(options['hit_count'])

            for key, value in counter.items():
                sieve.sift(value, key)

            for i in sieve.winners():
                callback({"score": i[0], 'document': self._corpus.get_document(i[1])})
        else:
            return None
