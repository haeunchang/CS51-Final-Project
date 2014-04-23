# This module contains functions for interacting with several external databases - dictionaries

import curses
from curses.ascii import isdigit
import nltk
from nltk.corpus import cmudict
 
d = cmudict.dict() 

def syllablecnt (word):
    """Returns the number of syllables in a word."""
    return [len(list(y for y in x if isdigit(y[-1]))) for x in d[word.lower()]]

def wordtype (word):
    """Returns the lexical category of a word (part of speech)."""
    raise NotImplementedError
