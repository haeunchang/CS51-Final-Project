class Line_type:
    def __init__(self, abstract_line, typenum):
        """Takes in an array whose elements are (word type, number of syllables)."""
        self.typenum = typenum
        self.typearray = [a[0] for a in abstract_line]
        self.syllablearray = [a[1] for a in abstract_line]
        self.skeleton = (abstract_line, typenum)
        self.occurrences = 0 # counts the number of occurrences of this line_type

    def __eq__(self, other):
        return self.skeleton == other.skeleton

    def __hash__(self):
        return hash(self.skeleton)
    
    def update(self):
        """Increases self_occurrences based on data from haiku."""
        self.occurrences += 1
       
    def get_occurrences (self):
        return self.occurrences
