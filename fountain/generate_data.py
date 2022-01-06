"""Process and compile static language data.

This only needs to be run once.
"""
from pathlib import Path

from . import file_io


def clean_norvig_src(contents: tuple) -> filter:
	"""Extract five-letter words from the Norvig word-count list."""
	return 	sorted(
		filter(
			lambda word: len(word) == 5,
			map(
				lambda line: line.split('\t')[0].lower(),
				contents
			)
		)
	)


def build_norvig_wordlist() -> None:
	"""Write out five-letter words in the Norvig/Google Books Ngram corpus."""
	src = file_io.read('fountain/data/src/norvig_google-books-common-words.txt')
	file_io.write(
		'fountain/data/norvig_wordlist.txt',
		clean_norvig_src(src)
	)


def main() -> None:
	"""Generate all static data."""
	print("\nRegenerating data:\n------------------")
	print("Building Norvig wordlist...", end=" ")
	build_norvig_wordlist()
	print("[ BUILT ]\n")


def has_all_static_data() -> None:
	"""Ensure that all static data exists."""
	return all(
		(
			Path(f"fountain/data/{filename}.txt").exists()
			for filename in ("knuth_wordlist", "norvig_wordlist")
		)
	)
