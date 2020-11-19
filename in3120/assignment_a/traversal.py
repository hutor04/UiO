#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Iterator
from invertedindex import Posting


class PostingsMerger:
    """
    Utility class for merging posting lists.
    """

    @staticmethod
    def intersection(p1: Iterator[Posting], p2: Iterator[Posting]) -> Iterator[Posting]:
        """
        A generator that yields a simple AND of two posting lists, given
        iterators over these.

        The posting lists are assumed sorted in increasing order according
        to the document identifiers.
        """

        posting_1 = next(p1, None)
        posting_2 = next(p2, None)

        while posting_1 and posting_2:
            if posting_1.document_id == posting_2.document_id:
                yield posting_1
                posting_1 = next(p1, None)
                posting_2 = next(p2, None)
            elif posting_1.document_id < posting_2.document_id:
                posting_1 = next(p1, None)
            else:
                posting_2 = next(p2, None)

    @staticmethod
    def union(p1: Iterator[Posting], p2: Iterator[Posting]) -> Iterator[Posting]:
        """
        A generator that yields a simple OR of two posting lists, given
        iterators over these.

        The posting lists are assumed sorted in increasing order according
        to the document identifiers.
        """

        posting_1 = next(p1, None)
        posting_2 = next(p2, None)

        while posting_1 or posting_2:
            if posting_1 is None and posting_2 is not None:
                yield posting_2
                posting_2 = next(p2, None)
            elif posting_2 is None and posting_1 is not None:
                yield posting_1
                posting_1 = next(p1, None)
            else:
                if posting_1.document_id == posting_2.document_id:
                    yield posting_1
                    posting_1 = next(p1, None)
                    posting_2 = next(p2, None)
                elif posting_1.document_id < posting_2.document_id:
                    yield posting_1
                    posting_1 = next(p1, None)
                else:
                    yield posting_2
                    posting_2 = next(p2, None)
