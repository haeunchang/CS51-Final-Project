class Dictionary
 
import curses
from curses.ascii import isdigit
import nltk
from nltk.corpus import cmudict
 
d = cmudict.dict() 
def return_syllable (word):
    return [len(list(y for y in x if isdigit(y[-1]))) for x in d[word.lower()]]# str -> int

def return_wordtype (string s): bool list
