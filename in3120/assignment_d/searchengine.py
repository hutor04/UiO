#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import Counter
from utilities import Sieve
from ranking import Ranker
from corpus import Corpus
from invertedindex import InvertedIndex
from typing import Callable, Any
from tokenization import ShingleGenerator


class SimpleSearchEngine:
    """
    A simple implementation of a search engine based on an inverted index, suitable for small corpora.
    """

    def __init__(self, corpus: Corpus, inverted_index: InvertedIndex):
        self._corpus = corpus
        self._inverted_index = inverted_index

    def _check_matches(self, fronture, n):
        """
        Finds duplicate document ID (matches) in fronture, and returns the list of
        respective fronture keys.
        """
        inv_dict = {}

        for key, value in fronture.items():
            inv_dict.setdefault(value.document_id, set()).add(key)

        result = list(filter(lambda x: len(x) >= n, inv_dict.values()))

        if len(result) > 0:
            return list(result[0])
        else:
            return []

    def _intersection(self, postings, n):
        results = []

        fronture = {i: next(posting, None) for i, posting in enumerate(postings)}

        #  Remove initially dead posting lists
        fronture = {k: v for k, v in fronture.items() if v is not None}

        while len(fronture) >= n:

            #  Find matching doc ids
            matches = self._check_matches(fronture, n)
            if len(matches) >= n:
                intermediate_result = {key: fronture[key] for key in matches}
                if len(results) > 0:
                    #  Remove dublicates
                    if results[-1] != intermediate_result:
                        results.append(intermediate_result)
                else:
                    results.append(intermediate_result)

            #  Minimal doc ID
            min_id = min(fronture, key=lambda x: fronture.get(x).document_id)

            #  Update fronture
            fronture[min_id] = next(postings[min_id], None)

            #  Remove dead posting lists
            fronture = {k: v for k, v in fronture.items() if v is not None}

        return results

    def evaluate(self, query: str, options: dict, ranker: Ranker, callback: Callable[[dict], Any]) -> None:
        """
        Evaluates the given query, doing N-out-of-M ranked retrieval. I.e., for a supplied query having M terms,
        a document is considered to be a match if it contains at least N <= M of those terms.

        The matching documents are ranked by the supplied ranker, and only the "best" matches are returned to the
        client via the supplied callback function.

        The client can supply a dictionary of options that controls this query evaluation process: The value of
        N is inferred from the query via the "match_threshold" (float) option, and the maximum number of documents
        to return to the client is controlled via the "hit_count" (int) option.

        The callback function supplied by the client will receive a dictionary having the keys "score" (float) and
        "document" (Document).
        """
        #  Query terms

        terms_multiplicity = Counter([term for term in self._inverted_index.get_terms(query)])
        terms = [term for term in terms_multiplicity.keys()]
        number_of_terms = len(terms)

        # Threshold
        n = max(1, min(number_of_terms, int(options['match_threshold'] * number_of_terms)))

        # Postings
        postings = [self._inverted_index.get_postings_iterator(i) for i in terms]

        # Here we search
        search_results = self._intersection(postings, n)
        search_results.sort(key=lambda x: len(x), reverse=True)

        # Ranking and Sieving
        sieve = Sieve(options['hit_count'])
        dedupe_docs = []

        for result in search_results:
            current_doc_id = result[list(result.keys())[0]].document_id
            if current_doc_id in dedupe_docs:
                pass

            else:
                dedupe_docs.append(current_doc_id)
                ranker.reset(current_doc_id)

                for key, value in result.items():
                    ranker.update(terms[key], terms_multiplicity[terms[key]], value)

                sieve.sift(ranker.evaluate(), current_doc_id)

        w = list(sieve.winners())

        # Return results
        for i in w:
            callback({'score': i[0], 'document': self._corpus.get_document(i[1])})
