class Bi_Gram:
    """A bi-gram will store pair occurrences in the training data."""
    
    def __init__(self, word1, word2):
        self.phrase = (word1, word2) # the word phrase
        self.occurrences = 0 # counts occurrences
    
    def update(self, haiku):
        """Increases self.occurrences based on data from haiku."""
        for line in haiku.lines:
            words = line.split()
            for i in range(len(words)-1):
                if (words[i],words[i+1]) == self.phrase:
                    self.occurrences += 1
        

