from monogram import Monogram
from bigram import Bi_Gram
from haiku import Haiku
from line_type import Line_type

class Training:
    def textconversion(haikus_text):
        """Returns a list of haikus, given a large text file."""

    def train_haiku(haiku, monograms, bi-grams, line_types):
        """Takes in a new Haiku as well as three sets: one of Monogram objects, one of Bi-Gram objects,
        and one of Line_type objects. Updates the three sets, returns None."""

        for line in haiku.lines:
            words = line.split()
            abstract_words = ([(dictionary.wordtype(a),
               dictionary.syllablecnt(a)) for a in words], line.typenum)
            if abstract_words == abstrlin.skeleton for some abstrlin in line_types:
                abstrlin.update()
            else:
                abstrlin = Line_type(abstract_words[0], abstract_words[1])
                abstrlin.update()
                line_types ADD abstrlin


            for i in range(len(words)-1):
                w = dictionary.word_filter(words[i])
                if dictionary.is_word(word):
                    if w == mono.word for some mono in monograms:
                        mono.update(haiku, line.typenum)
                    else:
                        new_mono = monogram(w)
                        new_mono.update(haiku, line.typenum)
                        monograms ADD new_mono
                        
                        
            for i in range(len(words)-2)
                (w_1, w_2)=(dictionary.word_filter(words[i]),
                            dictionary.word_filter(words[i+1]))
                if (dictionary.is_word(w_1) and dictionary.is_word(w_2)):
                    if w == bi.word for some bi in bigrams:
                        bi.update()
                    else:
                        new_bi = Bi_Gram(w_1, w_2)
                        new_bi.update()
                        bigrams ADD new_bi
            



    def train (haikus, monograms, bi-grams, line_types):
        """Trains the input haikus, updates monograms and bigrams, yields None"""
        train_haiku(x, monograms, bi-grams, line_types) for x in haikus

