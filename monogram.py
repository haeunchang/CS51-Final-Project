class Monogram:
    """A monogram will store most of the training data that we process. This will include
    the number of times it has occurred, its syllable count, word types, and a dictionary
    which returns other words that have appeared in the same haiku."""
    
    def __init__(self,word):
        self.word = word # the word itself
        self.syllables = -1 # syllable length, initialized to -1 indicating it has not been found
        self.wordtype = None # lexical category, bool list if found, initialized to None
        self.occurrences = 0 # counts the number of times word has occurred in the training data
    
    def get_length(self):
        """Returns the syllable length"
        if self.syllables == -1:
            self.syllables = dictionary.syllablecnt(self.word)
        return self.syllables
    
    def get_type(self):
        """Returns a bool list representing the word's type."""
        if self.wordtype == None:
            self.wordtype = dictionary.wordtype(self.word)
        return self.wordtype

    def adj_dict(self,word2):
        """Returns the adjacency coefficient of (self.word, word2)."""
        raise NotImplementedError
    
    def update(self,haiku):
        """Updates self.occurrences and self.adj_dict based on data from haiku."""
        raise NotImplementedError

