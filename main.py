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

my_total_population = 20
my_mutation_parameter = 0.3
my_cross_pollination_parameter = 0.4
a = 0.5
A = 1
B = 1
C = 1
number_of_generations = 5
monograms = {}
bigrams = {}
line_types = {}

def main():
    training.train(dictionary.read_input("data.txt"), monograms, bigrams, line_types)
    # print ([x for x in monograms])
    the_Haiku_Population = evolve_population.Evolve_population(my_total_population, my_mutation_parameter, my_cross_pollination_parameter, monograms, bigrams, line_types, a, A, B, C)
    for i in range (0, number_of_generations):
        the_Haiku_Population.update_next_generation()
    
    # print the haikus please    
    #the_Haiku_Population.population_list will be a list of evo objects
    for haiku in the_Haiku_Population.population_list:
        print (haiku)
    return 0

if __name__ == '__main__':
    main()
