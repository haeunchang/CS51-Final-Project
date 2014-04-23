class Population_haiku:
    def __init__(self, train_graph_mono, train_graph_bi, pop_size):
        """Spawns initial population based on the given training data.
        Pop_size is the size of the population.
        Takes in a random template, populates it with words."""
        self.population 

    def mutate(target_population):
        """The method has signature: int -> population_haiku and uses self.population
        Given the base population (self.populaton) and the target number of haikus,
        generate such number of mutated haikus
        accesses the haiku's score: the more successful a haiku is, 
        the more likely it will be the base for a mutation
        once the population is generated, class evaluate function
        to assign score"""

    def pollinate(target_population):
        """Again has the signature: int -> population_haiku and uses self.population
        Also accesses the haiku's score to randomly generate next generation."""

    def merge (self, population1, population2):
        """Merges two populations, returns merged population."""

    def evolve (self, mutateprob, pollinateprob):
        """Changes self.population by calling mutate and pollinate
        in the ratio defined by the mutateprob, pollinateprob parameters"""
