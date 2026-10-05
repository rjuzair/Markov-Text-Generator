#!/usr/bin/env python3
"""Generate text with a first-order Markov chain trained on a text file.

Usage:
    ./generate_text.py <input_file> <start_word> <max_words>

Each next word is sampled in proportion to how often it follows the current
word in the source text. Generation stops early if the chain reaches a word
that is never followed by another word.
"""
import os
import random
import sys

import text_stats


def generate(successors, start_word, max_words, rng=random):
    """Return up to `max_words` generated words, starting from `start_word`."""
    current = start_word.lower()
    output = [current]
    for _ in range(max_words):
        following = successors.get(current)
        if not following:
            break
        current = rng.choices(list(following), weights=list(following.values()), k=1)[0]
        output.append(current)
    return output


def main(argv):
    if len(argv) != 4:
        sys.exit(__doc__)
    path, start_word, max_words = argv[1], argv[2], argv[3]
    if not os.path.isfile(path):
        sys.exit(f"File not found: {path}")
    if not max_words.isdigit():
        sys.exit("max_words must be a positive integer")

    words = text_stats.all_words(text_stats.read_lines(path))
    successors = text_stats.successor_counts(words)
    if start_word.lower() not in successors:
        sys.exit(f"'{start_word}' does not appear in {path} (or is never followed by another word)")

    print(" ".join(generate(successors, start_word, int(max_words))))


if __name__ == "__main__":
    main(sys.argv)
