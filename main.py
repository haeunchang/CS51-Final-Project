#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2014 The Haiku Team
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
import evolve_population
import training
import dictionary
import sys
import pickle

my_total_population = 100
my_mutation_parameter = 0.3
my_cross_pollination_parameter = 0.4
a = 0.5
A = 1
B = 1
C = 1
number_of_generations = 20
monograms = {}
bigrams = {}
line_types = {}

def train():
    training.train(dictionary.read_input("data.txt"), monograms, bigrams, line_types)
    pickle.dump(monograms, open( "monograms.p", "wb"))
    pickle.dump(bigrams, open( "bigrams.p", "wb"))
    pickle.dump(line_types, open("line_types.p", "wb"))

def generate():
    monograms = pickle.load( open("monograms.p", "rb"))
    bigrams = pickle.load( open("bigrams.p", "rb"))
    line_types = pickle.load( open("line_types.p", "rb"))
    
    the_Haiku_Population = evolve_population.Evolve_population(my_total_population, my_mutation_parameter, my_cross_pollination_parameter, monograms, bigrams, line_types, a, A, B, C)
    for i in range (0, number_of_generations):
        the_Haiku_Population.update_next_generation()
    
    # print the haikus please    
    #the_Haiku_Population.population_list will be a list of evo objects
    for haiku in the_Haiku_Population.population_list:
        print (haiku)

def main(argv):
    if len(argv) > 0:
        if argv[0] == "train":
            train()
        elif argv[0] == "generate":
            generate()
    return 0

if __name__ == '__main__':
    main(sys.argv[1:])
