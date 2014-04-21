class population_haiku
	def __init__(train_graph_mono, train_graph_bi, pop_size):
    	#spawns initial population based on the given training data
        #pop_size is the size of the population
        #Takes in a random template, populates it with words
        self.population 
           
    def mutate(self.population, target_population):
    	#the method has signature: population_haiku * int -> population_haiku
        #Given the base population and the target number of haikus,
        #generate such number of mutated haikus
        #accesses the haiku's score: the more successful a haiku is, 
        #the more likely it will be the base for a mutation
        #once the population is generated, class evaluate function
        #to assign score
    
    def self_pollinate(self.population, target_population):
    	#again has the signature: population_haiku * int -> population_haiku
        #also accesses the haiku's score to randomly generate next generation
    
    def merge (population1, population2):
    	# merges two populations, returns merged population
        
    def evolve (mutateprob, pollinateprob):
    # changes self.population by calling mutate and self_pollinate
    # in the ratio defined by the mutateprob, pollinateprob parameters
