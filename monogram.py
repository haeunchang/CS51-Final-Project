
class Monogram:	
    def __init__(string):
        # A monogram will store most of the training data that we process. This will include
        # the number of times it has occurred, its syllable count, word types, and a dictionary
        # which returns other words that have appeared in the same haiku.
        self.word = string #the word
        self.get_length() = Dictionary.return_syllable self.word
                          #returns the syllable length 
        self.get_type() = Dictionary.return_wordtype self.word
                        #returns a bool list representing the word's type
        self.occurrences #counts the number of times word has occurred in the training data
        self.adj_dict(word2) #returns the adjacency coefficient of (self.word, word2)
        self.update(haiku) #updates self.occurrences and self.adj_dict based on data from haiku


