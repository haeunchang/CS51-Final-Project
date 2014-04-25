# This module contains functions for interacting with several external databases - dictionaries

import curses
from curses.ascii import isdigit
import nltk
from nltk.corpus import cmudict
 
d = cmudict.dict() 

def word_filter (word):
    """Removes possessive from the end of the word for classification purposes"""
    if word.find("'s") == len(word)-2:
        return word[:len(word)-2]
    else:
        return word


def syllablecnt (word):
    """Returns the number of syllables in a word."""
    return [len(list(y for y in x if isdigit(y[-1]))) for x in d[word.lower()]]

def wordtype (word):
    """Returns the lexical category of a word (part of speech)."""
    raise NotImplementedError
    
def is_word (word)
    """Returns a boolean describing whether or not this word falls into
    any of the four wordtypes defined above"""
    return (dictionary.wordtype(w)[0] != False or 
    dictionary.wordtype(w)[1] != False or
	dictionary.wordtype(w)[2] != False or
	dictionary.wordtype(w)[3] != False)
