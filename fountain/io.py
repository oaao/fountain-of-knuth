"""File I/O handling."""
from pathlib import Path


def read_file(file: str) -> tuple[str]:
	"""Read a file and return its line contents as a tuple of strings."""
	path = Path(file).resolve()
	with open(path, "r", encoding="utf-8") as f:
		contents = tuple(f.read().splitlines())
	return contents
