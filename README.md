# Markov Chain Text Generator

A command-line tool that analyses a text corpus and generates new text with a **first-order Markov chain** — each next word is sampled in proportion to how often it follows the current word in the source. Trained here on the *Complete Works of William Shakespeare* (~960,000 words).

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)
![No dependencies](https://img.shields.io/badge/dependencies-none-brightgreen)

## Example
```console
$ ./generate_text.py shakespeare.txt king 60
king northumberland he catesby o heaven and see the wound there was not often beat
his nets first to death rather be a tongue shakes aloft far from my sir as thus
prince i'll mourn in so the world's diameter as drink the tears duke of the noble…
```

## Usage
No third-party packages are needed — only the Python standard library.

**Text statistics** — total and unique word counts, a letter-frequency table, and the five most common words with their three most frequent successors:
```bash
./text_stats.py shakespeare.txt                  # print to the terminal
./text_stats.py shakespeare.txt sample_stats.txt # write to a file
```
See [`sample_stats.txt`](sample_stats.txt) for the full Shakespeare report.

**Text generation** — `<file> <start word> <max words>`:
```bash
./generate_text.py shakespeare.txt king 500
```
On Windows use `python text_stats.py …` / `python generate_text.py …`.

## How it works
1. **Tokenise** — split lines into words, strip surrounding punctuation and lower-case them.
2. **Build the transition table** — a single pass over consecutive word pairs produces `word → Counter(next words)`.
3. **Generate** — starting from the given word, repeatedly sample the next word with `random.choices`, weighted by the transition counts, until the word limit is reached or the chain hits a word with no successors.

Building the table once makes every generation step a dictionary lookup instead of a scan of the whole corpus.

## Tests
```bash
cd tests && PYTHONPATH=.. python -m pytest
```

## Ideas for extension
- Higher-order chains (condition on the previous *n* words) for more coherent sentences.
- Keep punctuation and capitalisation as tokens to produce sentence boundaries.
- Seed option (`--seed`) for reproducible output.
