import random

import generate_text
import text_stats

LINES = ["The king is dead.\n", "Long live the king!\n", "The king, the queen.\n"]


def test_all_words_strips_punctuation_and_lowercases():
    assert text_stats.all_words(["Hello, World! -- ok\n"]) == ["hello", "world", "ok"]


def test_compute_stats():
    stats = text_stats.compute_stats(LINES)
    assert stats["total_words"] == 12
    assert stats["unique_words"] == 7
    assert stats["common_words"][0] == ("the", 4)
    assert stats["common_successors"]["the"][0] == ("king", 3)


def test_successors_of_last_word_do_not_crash():
    successors = text_stats.successor_counts(["a", "b", "a"])
    assert dict(successors["a"]) == {"b": 1}
    assert "missing" not in successors


def test_generate_follows_observed_transitions():
    words = text_stats.all_words(LINES)
    successors = text_stats.successor_counts(words)
    output = generate_text.generate(successors, "The", 50, rng=random.Random(0))
    assert output[0] == "the"
    for current, following in zip(output, output[1:]):
        assert following in successors[current]


def test_generate_stops_at_dead_end():
    successors = text_stats.successor_counts(["start", "end"])
    assert generate_text.generate(successors, "start", 10) == ["start", "end"]
