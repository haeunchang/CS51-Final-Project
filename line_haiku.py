import dictionary

class Line_Haiku:
    def __init__(self, y, typenum):
        # Takes in a string array (and haiku position) and outputs 
        self.typenum = typenum

        self.wordarray = y
        self.typearray = [dictionary.wordtype(a) for a in y]
        self.syllablearray = [dictionary.syllablecnt(a) for a in y]
