"""File I/O handling."""
from pathlib import Path


def get_wordlist(wordlist_path: str) -> tuple[str]:
	"""Process a wordlist file into a tuple of strings."""
	path = Path(wordlist_path).resolve()

	with open(path, "r", encoding="utf-8") as f:
		wordlist = tuple(f.read().splitlines())

	return wordlist
