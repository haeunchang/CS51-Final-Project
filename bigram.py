class Bi_Gram:
    """A bi-gram will store pair occurrences in the training data."""
    
    def __init__(self, word1, word2):
        self.phrase = (word1, word2) # the word phrase
        self.occurrences = 0 # counts occurrences

    def __eq__(self, other):
        return self.phrase == other.phrase

    def __hash__(self):
        return hash(self.phrase)
    
    def update(self):
        """Increases self.occurrences based on data from haiku."""
        self.occurrences += 1
        

