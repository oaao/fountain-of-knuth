"""File I/O handling."""
from typing import Any

from pathlib import Path


def read(file_path: str) -> tuple[str]:
	"""Read a file and return its line contents as a tuple of strings."""
	path = Path(file_path).resolve()
	with open(path, "r", encoding="utf-8") as f:
		contents = tuple(f.read().splitlines())
	return sorted(contents)


def write(file_path: str, contents: Any) -> None:
	"""Write contents to a file."""
	path = Path(file_path).resolve()
	with open(path, "w", encoding="utf-8") as f:
		for item in contents:
			f.write(f"{item}\n")
