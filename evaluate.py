# Here is where all of the functions related to evaluating a haiku are written

import nltk
from monogram import Monogram
from bigram import Bi_Gram
from line_type import Line_type
from collections import Counter
import dictionary

# computes the correlation coefficient of two monograms using 
# same-line occurrence count and same-haiku occurrence count
def mono_correlation (mono1, mono2, a):
    A=0
    if mono2.word in mono1.adj_dict:
        A = mono1.adj_dict[mono2.word][0] + a * mono1.adj_dict[mono2.word][1]
    B=0
    if mono1.word in mono2.adj_dict:
        B = mono2.adj_dict[mono1.word][0] + a * mono2.adj_dict[mono1.word][1]
    return (A+B)/( (mono1.occurrences * mono2.occurrences)** .5)

# computes the total correlation of all pairs of monograms in a line (NOT line_haiku)
def line_mono_correlation (line, a, monograms): # line is just a list of words here
    total = 0
    word_count = 0
    for i in range(len(line)):
        if not dictionary.is_word(line[i]):
            continue
        word_count +=1
        for j in range(len(line)):
            if (i == j or not dictionary.is_word(line[j])):
                continue
            total += mono_correlation(monograms[line[i]],monograms[line[j]], a)
    if word_count <= 1:
        return 0
    return total/(word_count * (word_count-1))

# computes the bi-gram score of a line (simply averaging occurrences of all bi-grams)
def bi_gram_score (line, bi_grams): # line is still just a list of words
    total = 0
    for x in bi_grams:
        total += bi_grams[x].occurrences
    average = (total * 1.0) / len(bi_grams)
    
    total_count = 0
    count_valid = 0
    for i in range(len(line)-1):
        if (line[i], line[i+1]) in bi_grams:
            count_valid +=1
            total_count += bi_grams[(line[i], line[i+1])].occurrences
    if total_count == 0: 
        return 1
    else:
        return total_count * 1.0 / count_valid

def repetition_penalty (line, monograms): # penalizes line for repeated word
    my_line = [x for x in line if x in monograms]
    if len(my_line) == 0:
        return 0
    my_line_set = Counter(my_line)
    return float(my_line_set.most_common(1)[0][1]-1)/ len(my_line)

#def wordtype_bonus (line):
#    tagged_line = nltk.pos_tag(line)
#    tags = [nltk.pos_tag([word])[0] for word in line]
#    sum = 0
#    for i in range(len(line)):
#        if tagged_line[i][1] == tags[i][1]:
#            sum += 1
#    return sum

# returns a score for a triple of lines - will be used for evolution.
def evaluate(lines, monograms, bigrams, a, A, B, C, D):
    line_scores = [line_mono_correlation(line.wordarray, a, monograms) for line in lines]
    
    long_line = lines[0].wordarray+lines[1].wordarray+lines[2].wordarray
    threeline_score = line_mono_correlation(long_line, a, monograms)
    
    bigram_score = bi_gram_score(lines[0].wordarray, bigrams) + bi_gram_score(lines[1].wordarray, bigrams) + bi_gram_score(lines[2].wordarray, bigrams)
    
    penalty = repetition_penalty (lines[0].wordarray + lines[1].wordarray
               + lines[2].wordarray, monograms)

#    wt_bonus = wordtype_bonus(lines[0].wordarray) + wordtype_bonus(lines[1].wordarray) + wordtype_bonus(lines[2].wordarray)

    return (A*(line_scores[0]+line_scores[1]+line_scores[2]) +
            B* threeline_score + C * bigram_score - D * penalty)
