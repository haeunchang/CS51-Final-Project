import dictionary

class Line_Haiku:
    def __init__(self, y, typenum):
        # Takes in a string array (and haiku position) and outputs 
        self.typenum = typenum

        self.wordarray = y
        self.typearray = [dictionary.wordtype(a) for a in y]
        self.syllablearray = [dictionary.syllablecnt(a) for a in y]

    def __lt__(self, other):
        if self.typenum < other.typenum:
            return True
        elif other.typenum < self.typenum:
            return False
        elif self.wordarray < other.wordarray:
            return True
        return False
