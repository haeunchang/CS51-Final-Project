class Line_type:
    def __init__(self, abstract_line, typenum):
        """Takes in an array whose elements are (word type, number of syllables)."""
        self.typenum = typenum
        self.typearray = # list.map (fun (a, b) -> a) y
        self.syllablearray = # list.map (fun(a, b) -> b) y
        self.occurrences = 0 # counts the number of occurrences of this line_type
    
    def update(self,haiku):
        """Increases self_occurrences based on data from haiku."""
        raise NotImplementedError


