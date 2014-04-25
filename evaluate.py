from monogram import Monogram
from bigram import Bi_Gram
from line_type import Line_type
from haiku import Haiku

def mono_correlation (mono1, mono2, a) = 
    A = mono1.adj_dict[mono2.word]
    B = mono2.adj_dict[mono1.word]
    return (A+B)/( (mono1.occurrences * mono2.occurrences)** .5)

def line_mono_correlation (line, a): # line is a line_haiku object
    total = 0
    for i in range(len(line.wordarray)):
        for j in range(len(line.wordarray)):
            if i == j:
                continue
            total += mono_correlation(line.wordarray[i], line.wordarray[j], a)
    return total/(len(line.wordarray) * (len(line.wordarray)-1))

def bi_gram_count (line, bi_grams): #line is a line_haiku object
    total = 0
    for x in bi_grams:
        total += x.occurrences
    average = (total * 1.0) / len(
    

def evaluate(lines, monograms, bi_grams, a, c1, c2)
