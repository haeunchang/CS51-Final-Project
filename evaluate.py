"""Here is where all of the functions related to evaluating a haiku
   are written"""


from monogram import Monogram
from bigram import Bi_Gram
from line_type import Line_type
from haiku import Haiku

def mono_correlation (mono1, mono2, a) = 
    A = mono1.adj_dict[mono2.word]
    B = mono2.adj_dict[mono1.word]
    return (A+B)/( (mono1.occurrences * mono2.occurrences)** .5)

def line_mono_correlation (line, a): # line is just a list of words here
    total = 0
    for i in range(len(line)):
        for j in range(len(line)):
            if i == j:
                continue
            total += mono_correlation(line[i], line[j], a)
    return total/(len(line) * (len(line)-1))

def bi_gram_score (line, bi_grams): # line is just a list of words here
    total = 0
    for x in bi_grams:
        total += x.occurrences
    average = (total * 1.0) / len(bi_grams)
    
    total_count = 0
    count_valid = 0
    for i in range(len(line)-1):
        if dictionary.is_word(line[i]) and dictionary.is_word(line[i+1}):
            count_valid +=1
            total_count += bi_grams[(line[i], line[i+1])].occurrences
    if total_count = 0: 
        return 1
    else:
        return total_count * 1.0 / count_valid
        
def evaluate(lines, monograms, bi_grams, a, A, B, C):
    line_scores = [line_mono_correlation(line, a) for line in lines]
    
    long_line = line[0]+line[1]+line[2]
    threeline_score = line_mono_correlation(long_line, a)
    
    bigram_score = bi_gram_score(line[0]) + bi_gram_score(line[1])
                   + bi_gram_score(line[2])
    
    return A*(line_scores[0]+line_scores[1]+line_scores[2]) +
           B* threeline_score + C * bigram_score 
