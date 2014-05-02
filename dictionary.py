# This module contains functions for interacting with several external databases - dictionaries

import evo_object
import curses
from curses.ascii import isdigit
import nltk
from nltk.corpus import cmudict
from nltk.corpus import wordnet
from hyphen import Hyphenator, dict_info

d = cmudict.dict() 
h = Hyphenator('en_US')

def word_filter (word):
    """Removes possessive from the end of the word for classification purposes"""
    if word.find("'s") == len(word)-2:
        return word[:len(word)-2]
    if word.find("'") == len(word)-1:
        return word[:len(word)-1]
    return word

def syllablecnt (word):
    """Returns the number of syllables in a word."""
    if word.lower() in d:
        counts = [len(list(y for y in x if isdigit(y[-1]))) for x in d[word.lower()]]
        if len(counts) > 0:
            return counts[0]
    return len(h.syllables(word+' '))

def wordtype (word):
    """Returns the lexical category of a word (part of speech)."""
    types = [False, False, False, False, word]
    if word == "":
        return tuple(types)
    s = nltk.pos_tag(nltk.word_tokenize(word))[0][1]
    if s in set(["DT", "CC", "IN", "RP", "TO", "PRR", "PRP", "PRP$"]):
        return tuple(types)
    wntypes = wordnet.synsets(word)
    if len(wntypes) > 0:
        t = [synset.pos() for synset in wntypes[:int(round(len(wntypes)/2))+1]]
        if 'n' in t:
            types[0] = True
        if 'v' in t:
            types[1] = True
        if 's' in t:
            types[2] = True
        if 'r' in t:
            types[3] = True
        if True in types:
            types[4] = ""
        return tuple(types)
    return (True, False, False, False, "") # words not found are nouns

def is_word(word):
    """Returns a boolean describing whether or not this word falls into
    any of the four wordtypes defined above"""
    return (True in (wordtype(word)))

def read_input(textfile):
    """Returns a list of Haiku objects"""
    fin = open(textfile, 'r')

    t = []
    punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"']
    for line in fin.read().split('\n'):
        phrases = line.split()
        words = []
        for phrase in phrases:
            for w in phrase.split('-'):
                new = "".join(ltr for ltr in w if ltr not in punctuation)
                if new:
                    words.append(new)
        if words:
            t.append(words)
        else:
            print("BLANK LINE NOOOOO")
            print(line)

    fin.close()

    haikus = []
    for i in range(int(round(len(t)/4))):
        haikus.append(evo_object.Evo_object(t[i*4+1],t[i*4+2],t[i*4+3],raw_lines = True))
        print ([[y.wordarray for y in x.triple] for x in haikus])
    return haikus
