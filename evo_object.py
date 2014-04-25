from line_haiku import Line_Haiku
import evaluate
import random

class Evo_object:
	def __init__(self, line1, line2, line3, raw_lines = False):
        if raw_line:
            line1 = Line_Haiku(line1, 1)
            line2 = Line_Haiku(line2, 2)
            line3 = Line_Haiku(line3, 3)
            
		self.triple = [line1, line2, line3]
        self.score = 0
    	    
    def get_score (self):
        return self.score

    def get_triple (self):
        return self.triple
    
    def mutate_score(self, evaluated_score):
        self.score = evaluated_score

## ANCILLARY FUNCTIONS
    	
def compare(x, y):
    return(x.get_score() - y.get_score())

def cross_pollinate (evo_object1, evo_object2):
    new_triple = []
    for y in range(0, 2):
        if random.randint(0,1) == 0:
            new_triple.append(evo_object1.get_triple[y])
        else:
            new_triple.append(evo_object2.get_triple[y])
    new_kid = Evo_object(new_triple[0], new_triple[1], new_triple[2])
    return new_kid
    
def mutate (evo_object1)
    mutated_object = evo_object1
    return mutated_object
    
def gen_random_evo():
    raise NotImplementedError
#    random_object = Evo_object(random_triple, score)
#    return random_object
    
# Helper function that generates an element according to the probability in the array
# There is already a thing implemented in numpy, but hell

def random_weighted_occurrence (list_skeleton, list_weight):
    # assumes list1 is positive
    tot_sum = sum(list_weight)
    x = random.uniform(0, tot_sum)
    y = 0    
    while (True):
        if x < list_weight[y]:
            return list_skeleton[y]
        else:
            x = x - list_weight[y]
            y = y + 1

    
