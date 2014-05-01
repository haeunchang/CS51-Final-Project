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
import pickle
from optparse import OptionParser

my_total_population = 100
my_mutation_parameter = 0.3
my_cross_pollination_parameter = 0.4
a = 0.5
A = 1
B = 1
C = 1
D = 1
number_of_generations = 20
monograms = {}
bigrams = {}
line_types = {}

def load_train_files():
    global monograms, bigrams, line_types
    
    try:
        monograms = pickle.load( open("monograms.p", "rb"))
    except FileNotFoundError:
        print("Could not find monograms.p, creating new empty database.")
    try:
        bigrams = pickle.load( open("bigrams.p", "rb"))
    except FileNotFoundError:
        print("Could not find bigrams.p, creating new empty database.")
    try:
        line_types = pickle.load( open("line_types.p", "rb"))
    except FileNotFoundError:
        print("Could not find line_types.p, creating new empty database.")

def train(traindatafile):
    training.train(dictionary.read_input(traindatafile), monograms, bigrams, line_types)
    (monograms_file, bigrams_file, linetypes_file) = (open("monograms.p", "wb"), open("bigrams.p", "wb"), open("line_types.p", "wb"))
    pickle.dump(monograms, monograms_file)
    pickle.dump(bigrams, bigrams_file)
    pickle.dump(line_types, linetypes_file)
    monograms_file.close()
    bigrams_file.close()
    linetypes_file.close()

def generate():
    global monograms, bigrams, line_types

    load_train_files()

    the_Haiku_Population = evolve_population.Evolve_population(my_total_population, my_mutation_parameter, my_cross_pollination_parameter, monograms, bigrams, line_types, a, A, B, C, D)
    for i in range (0, number_of_generations):
        the_Haiku_Population.update_next_generation()
    
    # print the haikus please    
    #the_Haiku_Population.population_list will be a list of evo objects
    for haiku in the_Haiku_Population.population_list:
        print (haiku)

def main():
    parser = OptionParser()
    parser.add_option("-t", "--train", dest="training", action="store", type="string", default="",
                      help="train using data from FILE", metavar="FILE")
    parser.add_option("-g", "--generate", dest="generation", action="store_true", default=False,
                      help="generate new haikus using data aquired from training")
    parser.add_option("-f", "--fresh", dest="fresh_database", action="store_true", default=False,
                      help="overwrite old training databases (old information WILL be lost)")
    (options, args) = parser.parse_args()
    if options.training:
        if options.fresh_database:
            delete = input("Are you sure you want to delete old databases? [y/N] ")
            if delete.lower() != 'y':
                return 1
        else:
            load_train_files()
        train(options.training)
    if options.generation:
        generate()
    
    return 0

if __name__ == '__main__':
    main()
