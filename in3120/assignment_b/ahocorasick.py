#!/usr/bin/python
# -*- coding: utf-8 -*-

from tokenization import Tokenizer, BrainDeadTokenizer
# from utilities import apply
from typing import Optional, TypeVar, Callable, Any
from normalization import BrainDeadNormalizer

TrieType = TypeVar('Trie', bound='Trie')


class Trie:
    """
    A very simple and straightforward implementation of a trie for demonstration purposes
    and tiny dictionaries.

    A serious real-world implementation of a trie or an automaton would not be implemented
    this way. The trie/automaton would then instead be encoded into a single contiguous buffer
    and there'd be significant attention on memory consumption and scalability with respect to
    dictionary size.

    A node in the trie is also a trie itself in this implementation.
    """

    def __init__(self):
        self._children = {}

    def __repr__(self):
        return repr(self._children)

    def _add(self, string: str) -> None:
        assert 0 < len(string)
        trie = self
        for c in string:
            if c not in trie._children:
                trie._children[c] = Trie()
            trie = trie._children[c]
        trie._children[""] = Trie()

    def add(self, string: str, tokenizer: Tokenizer) -> None:
        """
        Adds the given string to the trie. The tokenizer is used so that we're robust
        to nuances in whitespace and punctuation. Use the same tokenizer throughout.
        """

        # TODO: Make the tokenizer a class variable.
        self._add(" ".join(tokenizer.strings(string)))

    def consume(self, prefix: str) -> Optional[TrieType]:
        """
        Consumes the given prefix, verbatim. If strings that have this prefix have been added to
        the trie, then the trie node corresponding to the prefix is returned. Otherwise, None is returned.
        """
        trie = self
        for c in prefix:
            if c in trie._children:
                trie = trie._children[c]
            else:
                return None
        return trie

    def is_final(self) -> bool:
        """
        Returns True iff the current node is a final/terminal state in the trie/automaton, i.e.,
        if a string has been added to the trie where the end of the string ends up in this node.
        """
        return "" in self._children


class StringFinder:
    """
    Given a trie encoding a dictionary of strings, efficiently finds the subset of strings in the dictionary
    that are also present in a given text buffer. I.e., in a sense computes the "intersection" or "overlap"
    between the dictionary and the text buffer.

    Uses a trie-walk algorithm similar to the Aho-Corasick algorithm with some minor NLP extensions. The
    running time of this algorithm is virtually independent of the size of the dictionary, and linear in
    the length of the buffer we are searching in.

    The tokenizer we use when scanning the input buffer is assumed to be the same as the one that was used
    when adding strings to the trie.
    """

    def __init__(self, trie: Trie, tokenizer: Tokenizer):
        self._trie = trie
        self._tokenizer = tokenizer

    def scan(self, buffer: str, callback: Callable[[dict], Any]) -> None:
        """
        Scans the given buffer and finds all dictionary entries in the trie that are also present in the
        buffer. We only consider matches that begin and end on token boundaries.

        The matching dictionary entries, if any, are reported back to the client via the supplied callback
        function.

        The callback function supplied by the client will receive a dictionary having the keys "match" (str) and
        "range" (Tuple[int, int]).

        In a serious application we'd add more lookup/evaluation features, e.g., support for prefix matching,
        support for leftmost-longest matching (instead of reporting all matches), and support for lemmatization
        or similar linguistic variations.
        """
        default_padding = 2
        normalizer = BrainDeadNormalizer()

        buffer = normalizer.normalize(buffer)
        buffer = ' '.join(buffer.split())  # Removes double whitespaces. There is a case in test input.
        ranges = self._tokenizer.ranges(buffer)

        def _find_phrases(index: int, padding: int) -> None:
            """
            Helper function used match phrases.
            :param index: int
                        start index
            :param padding: int
                        padding
            :return: None
            """
            if index + padding > len(ranges):
                return
            r = ranges[index:index + padding]
            s, e = (r[0][0], r[-1][1])
            txt = buffer[s:e]
            print(text)
            trie = self._trie.consume(txt)
            if trie is None:
                return
            elif t.is_final():
                callback({'match': txt, 'range': (s, e)})
                _find_phrases(index, padding + 1)

        for i, rng in enumerate(ranges):
            start, end = rng
            text = buffer[start:end]
            t = self._trie.consume(text)

            if t is None:
                pass
            elif t.is_final():
                callback({'match': text, 'range': rng})
                if t.consume(' ') is not None:
                    _find_phrases(i, default_padding)


def main():
    """
    Example usage. A tiny unit test, in a sense.
    """
    tokenizer = BrainDeadTokenizer()
    strings = ["abba", "ørret", "abb", "abbab", "abbor"]
    trie = Trie()
    for s in strings:
        trie.add(s, tokenizer)
    assert trie.is_final() is False
    assert trie.consume("snegle") is None
    node = trie.consume("ab")
    assert node.is_final() is False
    node = node.consume("b")
    assert node.is_final() is True
    assert node == trie.consume("abb")


if __name__ == "__main__":
    main()
