from line_haiku import Line_Haiku
import evaluate
import random
import training
import line_type

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
    
    def update_score(self, evaluated_score):
        self.score = evaluated_score

## ANCILLARY FUNCTIONS

## HELPER FUNCTIONS

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

def populate_words (a_line_type, monograms):
    my_skeleton = a_line_type.skeleton[0]
    my_line = []
    for i in range(len(my_skeleton)):
        if my_skeleton[i][0][4] =="" :
            word_list = [x for x in monograms if (monograms[x].wordtype == my_skeleton[i][0]) & (monograms[x].syllables == my_skeleton[i][1]]
            word_weight = [word_list[x].occurrences for x in word_list]
            # randomly generates a fitting monogram
            my_line.append(random_weighted_occurrence (word_list, word_weight))
        else:
            my_line.append (my_skeleton[i][0][4])
                	
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
    
def mutate_line (my_line, monograms):
    new_line = my_line
    k = random.randint(0,len(my_line)-1)
    while not(dictionary.is_word(my_line[k])):
        k = random.randint(0, len(my_line)-1)
    word_list = [x for x in monograms if (x.wordtype == monograms[my_line[k]].wordtype) & (x.syllables == monograms[my_line[k]].syllables)]
    word_weight = [word_list[x].occurrences for x in word_list]
    generated_word = random_weighted_occurrence (word_list, word_weight)
    new_line[k] = generated_word
    return new_line
    
    
    
def mutate (evo_object1, monograms):
    line_index_to_mutate = random.randint(0, 2)
    mutated_object = evo_object1
    mutated_object.triple[line_index_to_mutate] = mutate_line(mutated_object.triple[line_index_to_mutate], monograms) 
    return mutated_object
    
def gen_random_evo(monograms, bigrams, line_types, a, A, B, C):
    # generates random skeleton for each type
    list_skeleton_1 = [x for x in line_types if line_types[x].typenum == 1]
    list_weight_1 = [line_types[x].occurrences for x in list_skeleton_1]
    random_line_type_1 = random_weighted_occurrence(list_skeleton_1, list_weight_1)
    my_line_1 = populate_words (random_line_type_1, monograms)
    
    list_skeleton_2 = [x for x in line_types if line_types[x].typenum == 2]
    list_weight_2 = [line_types[x].occurrences for x in list_skeleton_2]
    random_line_type_2 = random_weighted_occurrence(list_skeleton_2, list_weight_2)
    my_line_2 = populate_words (random_line_type_2, monograms)
    
    list_skeleton_3 = [x for x in line_types if line_types[x].typenum == 3]
    list_weight_3 = [line_types[x].occurrences for x in list_skeleton_3]
    random_line_type_3 = random_weighted_occurrence(list_skeleton_3, list_weight_3)
    my_line_3 = populate_words (random_line_type_3, monograms)
    
    my_random_haiku = Evo_object([my_line_1, my_line_2, my_line_3)
    my_random_haiku.update_score(evaluate.evaluate([my_line_1, my_line_2, my_line_3], monograms, bigrams, a, A, B, C)
    
    return my_random_haiku  

        

    
