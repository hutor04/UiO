#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class Normalizer(ABC):
    """
    Simple abstract base class for text normalizers.
    """

    @abstractmethod
    def canonicalize(self, buffer: str) -> str:
        """
        Normalizes a larger text buffer, so that downstream NLP can assume some kind of
        standardized text representation.

        In a serious application we might normalize the encoding and do Unicode canonicalization
        here, and perhaps nothing else.
        """
        pass

    @abstractmethod
    def normalize(self, token: str) -> str:
        """
        Normalizes a token to produce an actual index term.

        In a serious application we might do transliteration, accent removal, lemmatization or
        stemming, or other stuff here, in addition to simple case folding.
        """
        pass


class BrainDeadNormalizer(Normalizer):
    """
    A dead simple normalizer for simple testing purposes.
    """

    def __init__(self):
        pass

    def canonicalize(self, buffer: str) -> str:
        return buffer

    def normalize(self, token: str) -> str:
        return token.lower()


def main():
    """
    Example usage. A tiny unit test, in a sense.
    """
    normalizer = BrainDeadNormalizer()
    buffer = "Dette ER en\nprØve!"
    print(normalizer.canonicalize(buffer))
    token = "grØnnFustaSJEOpphengsForKOBling"
    print(normalizer.normalize(token))
    assert normalizer.normalize(token) == "grønnfustasjeopphengsforkobling"


if __name__ == "__main__":
    main()
