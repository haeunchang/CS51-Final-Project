from line_haiku import Line_Haiku
import evaluate
import random
import training
import line_type
import dictionary
from copy import deepcopy

class Evo_object:
    def __init__(self, line1, line2, line3, raw_lines = False):
        l1, l2, l3 = None, None, None
        if raw_lines:
            l1 = Line_Haiku(line1, 1)
            l2 = Line_Haiku(line2, 2)
            l3 = Line_Haiku(line3, 3)
        else:
            l1, l2, l3 = line1, line2, line3
        self.triple = [l1, l2, l3]
        self.score = 0

    def __lt__(self,other):
        if self.score > other.score:
            return True
        elif self.score < other.score:
            return False
        elif self.triple < other.triple:
            return True
        return False

    def __gt__(self,other):
        return other < self

    def __eq__(self,other):
        return (not (self < other)) and (not (other < self))

    def __str__(self):
        return ' / '.join([' '.join(line.wordarray) for line in self.triple])

    def get_score (self):
        return self.score

    def get_triple (self):
        return self.triple
    
    def update_score(self, evaluated_score):
        self.score = evaluated_score

## ANCILLARY FUNCTIONS

## HELPER FUNCTIONS

# Helper function that generates an element according to the probability 
# in the array

def random_weighted_occurrence (list_skeleton, list_weight):
    # assumes list_weight is positive
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
            word_list = [x for x in monograms if (
            (monograms[x].wordtype == my_skeleton[i][0]) and 
            (monograms[x].syllables == my_skeleton[i][1]))]

            word_weight = [monograms[x].occurrences for x in word_list]

            # if the word list is empty, blame insufficient training data
            if not word_list:
                print("The training data is not sufficient for populating the line types with words. Maybe you used -f too liberally?")
                exit()

            # randomly generates a fitting monogram
            my_line.append(random_weighted_occurrence (word_list, word_weight))
        else:
            my_line.append (my_skeleton[i][0][4])
    return Line_Haiku(my_line, a_line_type.typenum)
                	
def compare(x, y):
    return(x.get_score() - y.get_score())

def cross_pollinate (evo_object1, evo_object2, monograms, bigrams, a, A, B, C, D):
    new_triple = []
    for y in range(3):
        if random.randint(0,1) == 0:
            new_triple.append(evo_object1.get_triple()[y])
        else:
            new_triple.append(evo_object2.get_triple()[y])
    new_kid = Evo_object(new_triple[0], new_triple[1], new_triple[2])
    new_kid.update_score(evaluate.evaluate(new_kid.triple, monograms, bigrams,
                                           a, A, B, C, D))
    return new_kid
    
def mutate_line (my_linehaiku, monograms):
    my_line = my_linehaiku.wordarray
    new_line = my_line
    k = random.randint(0,len(my_line)-1)
    found_a_word = False
    for i in range(1000):
        if (dictionary.is_word(my_line[k])):
            found_a_word = True
            break
        k = random.randint(0, len(my_line)-1)
    if not found_a_word:
        return my_linehaiku # just give up

    word_list = [x for x in monograms if (monograms[x].wordtype == 
                monograms[my_line[k]].wordtype) & 
                (monograms[x].syllables == monograms[my_line[k]].syllables)]

    word_weight = [monograms[x].occurrences for x in word_list]
    generated_word = random_weighted_occurrence (word_list, word_weight)
    new_line[k] = generated_word
    return Line_Haiku(new_line, my_linehaiku.typenum)
    
    
    
def mutate (evo_object1, monograms, bigrams, a, A, B, C, D):
    line_index_to_mutate = random.randint(0, 2)
    mutated_object = deepcopy(evo_object1)

    mutated_object.triple[line_index_to_mutate] = mutate_line(
                   mutated_object.triple[line_index_to_mutate], monograms)

    mutated_object.update_score(evaluate.evaluate(mutated_object.triple,
                                         monograms, bigrams, a, A, B, C, D)) 
    return mutated_object
    
def gen_random_evo(monograms, bigrams, line_types, a, A, B, C, D):
    # generates random skeleton for each type
    list_skeleton_1 = [x for x in line_types if line_types[x].typenum == 1]
    list_weight_1 = [line_types[x].occurrences for x in list_skeleton_1]
    random_line_type_1 = line_types[random_weighted_occurrence(list_skeleton_1,
                                                               list_weight_1)]
    my_line_1 = populate_words (random_line_type_1, monograms)
    if my_line_1 == None: # failure when populating with words
        return None
    
    list_skeleton_2 = [x for x in line_types if line_types[x].typenum == 2]
    list_weight_2 = [line_types[x].occurrences for x in list_skeleton_2]
    random_line_type_2 = line_types[random_weighted_occurrence(list_skeleton_2,
                                                               list_weight_2)]
    my_line_2 = populate_words (random_line_type_2, monograms)
    if my_line_2 == None: # failure when populating with words
        return None
    
    list_skeleton_3 = [x for x in line_types if line_types[x].typenum == 3]
    list_weight_3 = [line_types[x].occurrences for x in list_skeleton_3]
    random_line_type_3 = line_types[random_weighted_occurrence(list_skeleton_3,
                                                               list_weight_3)]
    my_line_3 = populate_words (random_line_type_3, monograms)
    if my_line_3 == None: # failur when populating with words
        return None
    
    my_random_haiku = Evo_object(my_line_1, my_line_2, my_line_3)
    my_random_haiku.update_score(evaluate.evaluate([my_line_1, my_line_2,
                                 my_line_3], monograms, bigrams, a, A, B, C, D))
    
#    print ([l.wordarray for l in my_random_haiku.triple])
    return my_random_haiku  

def gen_random_markov (digrams):
    line_counter = 0
    # generates initial word
    starting_words = [(x[1], digrams[x]) for x in digrams if x[0] == "\n"]    
        
    starting_letters = [y[0] for y in starting_words]
    starting_weights = [y[1] for y in starting_words]
    my_word= random_weighted_occurrence(starting_letters, starting_weights)
            
    net_poem = []
    net_poem.append(my_word)
    while (line_counter < 3):
                
        potential_words = [(x[1], digrams[x]) for x in digrams if x[0] == my_word]
        next_letters = [y[0] for y in potential_words]
        next_weights = [y[1] for y in potential_words]
                
        next_word= random_weighted_occurrence(next_letters, next_weights)
        if next_word == "\n":
            line_counter = line_counter + 1
            
        net_poem.append(next_word)
        my_word = next_word  
    return(net_poem)  
        
     

    
