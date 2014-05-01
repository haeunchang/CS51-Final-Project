import dictionary

class Monogram:
    """A monogram will store most of the training data that we process. This will include
    the number of times it has occurred, its syllable count, word types, and a dictionary
    which returns other words that have appeared in the same haiku."""
    
    def __init__(self,word):
        self.word = word # the word itself
        self.syllables = dictionary.syllablecnt(self.word) #number of syllables
        self.wordtype = dictionary.wordtype(self.word) # lexical category
        self.occurrences = 0 # counts the number of times word has occurred in the training data
        self.adj_dict = {} # dictionary from adjacent word to adjancency coefficient

    def __eq__(self, other):
        return self.word == other.word

    def __hash__(self):
        return hash(self.word)
    
    def update_adj_dict(self,word2,same_line):
        """Returns the adjacency coefficient of (self.word, word2)."""
        if word2 in self.adj_dict:
            if same_line:
                self.adj_dict[word2] = (self.adj_dict[word2][0]+1,
                                        self.adj_dict[word2][1])
            else:
                self.adj_dict[word2] = (self.adj_dict[word2][0], 
                                        self.adj_dict[word2][1]+1)
        else:
            if same_line: 
                self.adj_dict[word2] = (1, 0)
            else:
                self.adj_dict[word2] = (0, 1)
    def update(self,haiku, typenum):
        """Updates self.occurrences and self.adj_dict based on data from haiku."""
        self.occurrences += 1
        for i in range(2):
            for x in (haiku.triple[i]).wordarray:
                if (self.wordtype == dictionary.wordtype(x) and 
                    dictionary.word_filter(x) != self.word):
                    self.update_adj_dict(x, i==typenum)
            

