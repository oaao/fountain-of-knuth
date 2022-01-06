"""Linguistic data for statistical pre-processing.


Frequency statistics, as seen in data/, are provided by:

a) Mark Mayzner, 1965:
------------------------------------------------------------------------------
METHODOLOGY: Starting at a random place in a given newspapers/magazines/book,
record three- to seven-letter words until 200 words are selected. Repeat 100x.

SAMPLE SIZE: 20,000
https://archive.is/wip/u9vOA (as seen in tables: https://archive.is/BJEQt)
------------------------------------------------------------------------------


b) Peter Norvig, 2012:
------------------------------------------------------------------------------
METHODOLOGY: Using the Google Books Ngrams dataset (English 20120701), perform
the analysis on the entire corpus, with no sample size or length restrictions.
Discard any word with fewer than 100,000 mentions.

SAMPLE SIZE: 743,842,922,321 (unique: 97,565)
https://archive.is/wip/SHwcy
Data available by substituting {a-z} for the final character in the URL:
https://storage.googleapis.com/books/ngrams/books/googlebooks-eng-all-1gram-20120701-a.gz
------------------------------------------------------------------------------
"""
import string


LETTERS = tuple(string.ascii_lowercase)
