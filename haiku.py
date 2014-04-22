class Haiku:
    def __init__(self, line1, line2, line3):
        # Haikus have an array of line objects of size 3
        self.line[0] = line1
        self.line[1] = line2
        self.line[2] = line3
        self.score = 0 #describes the score of the haiku
    
    def mutate (self, x, line):
        self.line[x] = line
        
    def update_score(self,evaluatedscore):
        self.score = evaluatedscore 
