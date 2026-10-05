#!/usr/bin/env python3
"""Print word and letter statistics for a text file.

Usage:
    ./text_stats.py <input_file> [output_file]

Reports the total and unique word counts, a letter frequency table, and the
five most common words together with their three most frequent successors.
If an output file is given, the report is written there instead of stdout.
"""
import collections
import os
import sys
from string import punctuation

NUM_COMMON_WORDS = 5
NUM_SUCCESSORS = 3


def all_words(lines):
    """Return every word in `lines`, lower-cased with surrounding punctuation removed."""
    words = (word.strip(punctuation).lower() for line in lines for word in line.split())
    return [word for word in words if word]


def letter_frequencies(words):
    """Return (letter, count) pairs for alphabetic characters, most common first."""
    return collections.Counter(ch for word in words for ch in word if ch.isalpha()).most_common()


def successor_counts(words):
    """Map each word to a Counter of the words that immediately follow it."""
    successors = collections.defaultdict(collections.Counter)
    for current, following in zip(words, words[1:]):
        successors[current][following] += 1
    return successors


def compute_stats(lines):
    words = all_words(lines)
    word_counts = collections.Counter(words)
    successors = successor_counts(words)
    common_words = word_counts.most_common(NUM_COMMON_WORDS)
    return {
        "total_words": len(words),
        "unique_words": len(word_counts),
        "letters": letter_frequencies(words),
        "common_words": common_words,
        "common_successors": {
            word: successors[word].most_common(NUM_SUCCESSORS) for word, _ in common_words
        },
    }


def format_report(stats):
    lines = [
        "******** File Stats ********",
        "",
        f"Total number of words: {stats['total_words']}",
        f"Total number of unique words: {stats['unique_words']}",
        "",
        "Letter frequency table:",
    ]
    lines += [f"  {letter} {count}" for letter, count in stats["letters"]]
    lines += ["", f"Top {NUM_COMMON_WORDS} most common words and their {NUM_SUCCESSORS} most common successors:"]
    for word, count in stats["common_words"]:
        lines.append(f"\n  {word} ({count} occurrences)")
        lines += [f"    -- {successor}  {n}" for successor, n in stats["common_successors"][word]]
    return "\n".join(lines)


def read_lines(path):
    with open(path, encoding="utf-8-sig") as input_file:
        return input_file.readlines()


def main(argv):
    if len(argv) not in (2, 3):
        sys.exit(__doc__)
    if not os.path.isfile(argv[1]):
        sys.exit(f"File not found: {argv[1]}")

    report = format_report(compute_stats(read_lines(argv[1])))

    if len(argv) == 3:
        with open(argv[2], "w", encoding="utf-8") as output_file:
            output_file.write(report + "\n")
        print(f"Text stats written to {argv[2]}")
    else:
        print(report)


if __name__ == "__main__":
    main(sys.argv)
