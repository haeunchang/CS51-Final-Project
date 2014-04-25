# This module contains functions for interacting with several external databases - dictionaries

import curses
from curses.ascii import isdigit
import nltk
from nltk.corpus import cmudict
from nltk.corpus import wordnet
from hyphen.dictools import 
from hyphen import Hyphenator, dict_info

d = cmudict.dict() 
h = Hyphenator('en_US')

def word_filter (word):
    """Removes possessive from the end of the word for classification purposes"""
    if word.find("'s") == len(word)-2:
        return word[:len(word)-2]
    else:
        return word

def syllablecnt (word):
    """Returns the number of syllables in a word."""
    if word.lower() in d:
        counts = [len(list(y for y in x if isdigit(y[-1]))) for x in d[word.lower()]]
        if len(counts) > 0:
            return counts[0]
    return h.syllables(word)

def wordtype (word):
    """Returns the lexical category of a word (part of speech)."""
    wntypes = wordnet.synsets(word)
    if len(wntypes) > 0:
        t = [synset.pos() for synset in wntypes[:len(wntypes)/2+1]
        types = [False, False, False, False, word]
        if 'n' in t:
            types[0] = True
        if 'v' in t:
            types[1] = True
        if 's' in t:
            types[2] = True
        if 'r' in t:
            types[3] = True
        return types
    return None

def is_word (w):
    """Returns a boolean describing whether or not this word falls into
    any of the four wordtypes defined above"""
    return (True in dictionary.wordtype(w))
