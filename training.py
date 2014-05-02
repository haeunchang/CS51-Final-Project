from monogram import Monogram
from bigram import Bi_Gram
from line_type import Line_type
import evo_object
import dictionary

def train_haiku(haiku, monograms, bigrams, digrams, line_types):
    """Takes in a new Haiku as well as three dictionaries: one of 
    Monogram objects (keys are words), one of Bi-Gram objects (keys are
    phrases), and one of Line_type objects (keys are skeletons). 
    Updates the three dictionaries, returns None."""

    for line in haiku.triple:
        words = line.wordarray
        abstract_skeleton = (tuple((tuple(dictionary.wordtype(a)),
           dictionary.syllablecnt(a)) for a in words), line.typenum)
        if abstract_skeleton in line_types:
            line_types[abstract_skeleton].update()
        else:
            abstrlin = Line_type(abstract_skeleton[0], abstract_skeleton[1])
            abstrlin.update()
            line_types[abstrlin.skeleton] = abstrlin


        for i in range(len(words)):
            w = dictionary.word_filter(words[i])
            if dictionary.is_word(w):
                # print (w, "is a word")
                if w in monograms:
                    monograms[w].update(haiku, line.typenum)
                else:
                    new_mono = Monogram(w)
                    new_mono.update(haiku, line.typenum)
                    monograms[w] = new_mono
                    
        #if len(words) == 0:
        #    print("empty word")
        #    exit()         
        for i in range(len(words)):
            if i < len(words)-1:
                (w_1, w_2)=(dictionary.word_filter(words[i]),
                            dictionary.word_filter(words[i+1]))
                
                if i == 0:
                    #if w_1 == "":
                    #    print("empty filtered word")
                    #    print(words)
                    
                    if ("\n", w_1) in digrams:
                        digrams[("\n", w_1)] += 1
                    else: 
                        digrams[("\n", w_1)] = 1
                
                if (w_1, w_2) in digrams:
                    digrams[(w_1, w_2)] += 1
                else:
                    digrams[(w_1, w_2)] = 1

                if (dictionary.is_word(w_1) and dictionary.is_word(w_2)):
                    if (w_1, w_2) in bigrams:
                        bigrams[(w_1, w_2)].update()
                    else:
                        new_bi = Bi_Gram(w_1, w_2)
                        new_bi.update()
                        bigrams[(w_1, w_2)] = new_bi
            else:
                w = dictionary.word_filter(words[i])
                if (w, "/n") in digrams:
                    digrams[(w, "\n")] +=1
                else:
                    digrams[(w, "\n")] = 1


def train (haikus, monograms, bigrams, digrams, line_types):
    """Trains the input haikus, updates monograms, bi-grams, 
       and line_types (which are dictionaries), yields None"""
    [train_haiku(x, monograms, bigrams, digrams, line_types) for x in haikus]

