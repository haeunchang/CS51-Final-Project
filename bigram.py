class Bi_Gram:
    """A bi-gram will store pair occurrences in the training data."""
    
    def __init__(self, word1, word2):
        self.phrase = (word1, word2) # the word phrase
        self.occurrences = 0 # counts occurrences
    
    def update(self):
        """Increases self.occurrences based on data from haiku."""
        self.occurrences += 1
        

