# Needs a evolve object
import evo_object as evo_object
import random
import math

class Evolve_population:

    population_list = []
    total_population = 0
    mutation_parameter = 0
    cross_pollination_parameter = 0
    
    # initializes population
    def __init__(self, my_total_population, my_mutation_parameter, my_cross_pollination_parameter):
        self.mutation_parameter = my_mutation_parameter
        self.cross_pollination_paramter = my_cross_pollination_parameter
        self.total_population = my_total_population
        for x in range (0, my_total_population):
            # Creates new object
            new_object = evo_object.gen_random_evo()
            self.population_list.append(new_object)
        # sorts the list
        self.population_list.sort(evo_object.compare)
            
    def update_next_generation(self)
        mutant_pop = int(self.total_population * self.mutation_parameter)
        cross_pop = int(self.total_population * self.cross_pollintion_parameter)
        prev_pop = self.population_list
        # Creates random pollination/mutation      
        for x in range (0, mutant_pop):
            new_mutant = create_mutants(prev_pop)
            self.population_list.append (new_mutant)
        for x in range (0, cross_pop):
            new_cross = create_cross_pollinated(prev_pop)
            self.population_list.append (new_cross)    
        # sorts it
        self.population.sort(evo_object.compare)
        # cuts off the least successful ones
        self.population_list = self.population_list [0: total_population]
       
# as of now, uniformly chooses elements to mutate
def create_mutants (base_population):
    x = random.randint(0, len(base_population)- 1)
    to_be_mutated = base_population[x]
    mutated_object = evo_object.mutate()
    return mutated_object

# similarly, uniformly chooses elements to cross_pollinate
# Note that if it chooses the same one, it will effectively replicate the said object, which is not bad
def create_cross_pollinated (base_population):
    x = random.randint(0, len(base_population) - 1)
    y = random.randint(0, len(base_population) - 1)
    pollinated_object = evo_object.cross_pollinate (base_population[x], base_population[y])
    return pollinated_object   

