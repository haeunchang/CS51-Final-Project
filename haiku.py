from line_haiku import Line_Haiku

class Haiku:
    def __init__(self, line1, line2, line3, raw_lines = False):
        if raw_line:
            line1 = Line_Haiku(line1, 1)
            line2 = Line_Haiku(line2, 2)
            line3 = Line_Haiku(line3, 3)
        
        # Haikus have an array of line objects of size 3
        self.lines = [line1, line2, line3]
        self.score = 0 #describes the score of the haiku
    
    def mutate (self, x, line):
        self.lines[x] = line
        
    def update_score(self, evaluatedscore):
        self.score = evaluatedscore
