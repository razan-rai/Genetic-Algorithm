#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 20:00:02 2019

@author: razan
"""
##Genetic Algorithm
class GeneticAlgorithm:
    def individual_with_gene_no(individual_no, gene_no):
        #fitness_function = '(x0+x1)-(x2+x3)+(x4+x5)'
        fitness_function = input('Enter the Fitness Function:')
        individual_dic = {} #individual dictionary
        fittest_individual = {} #fitness function evaluation result in dictionary
        chrosome_list = []
        for i in range(individual_no):
            chromosome = int(input('Enter a individuals chromosomes: '))
            fitness = obj.fitnessFunction_calculation(chromosome, gene_no, fitness_function)
            fittest_individual.update({'x'+str(i) : fitness})
            individual_dic.update({'x'+str(i) : chromosome})
            chrosome_list.append(chromosome)
        #individual sort in order
        sorted_list = [x for x in fittest_individual.items()]
        #sorted_list.sort(key=lambda x: x[0]) #sort by key
        sorted_list.sort(key=lambda x: x[1]) #sort by value
        print('Individual Fitness result in order:', sorted_list)
        
        #perfoming crossover
        obj.cross_over_evaluation(sorted_list, individual_dic)
        
        #Evaluating fitness of new population formed by the cross over 
        new_fitness_after_crossover = obj.evaluating_new_fitnessFunction(fitness_function, gene_no, chrosome_list)
        
        #comparing overall fitness before and after crossover
        #for i in range(len(fittest_individual)):
        print('Average of fitness:', sum(fittest_individual.values()))
        print('Average of fitness after crossover:', sum(new_fitness_after_crossover.values()))
            
    def evaluating_new_fitnessFunction(fitness_function, gene_no, chrosome_list):
        #first doing crossover
        new_crossover_individual = []
        for first_chromosome, second_chromosome in obj.grouped(chrosome_list, 2):
            l, r = str(first_chromosome)[:int(len(str(first_chromosome))/2)], str(first_chromosome)[int(len(str(first_chromosome))/2):]
            l2, r2 = str(second_chromosome)[:int(len(str(first_chromosome))/2)], str(second_chromosome)[int(len(str(first_chromosome))/2):]
            print('first crossover', l + r2)
            print('second crossover', l2 + r)
            new_crossover_individual.append(l + r2)
            new_crossover_individual.append(l2 + r)
        #now evaluating fitness function on crossover individual
        new_fittest_individual = {}
        for i in range(len(new_crossover_individual)):
            fitness = obj.fitnessFunction_calculation(new_crossover_individual[i], gene_no, fitness_function)
            new_fittest_individual.update({'x'+str(i) : fitness})
            
        print('new fittest individual:', new_fittest_individual)
        return new_fittest_individual
        
        
            
        
    def grouped(iterable, n):
        return zip(*[iter(iterable)]*n)  
    
    
    def fitnessFunction_calculation(chromosome, gene_no, fitness_function):
        #validation of input chromosome and gene number they should be equal
        if(len(str(chromosome)) == gene_no):
            #converting input string into dictionary
            x = {}
            for idx, val in enumerate(str(chromosome)):
                x.update({'x'+str(idx) : val})
            #evaluating fitness of every individual
            dic2 = x
            equation_string = fitness_function
            for k, v in dic2.items():
                equation_string = equation_string.replace(k, v) #replacing the fitness equation with gene
            print('Equivalent Fitness function:', equation_string)
            print('Equivalent Fitness function evaluation:', eval(equation_string))
            return eval(equation_string)
        else:
            print('Chromosome number and Gene number does not match.')
            return True
        
    def switcher(choice, sorted_list, individual_dic):
        if(choice <= 5):
            print('The choice is:', choice)
            if(choice == 0):
                obj.one_point_crossover(individual_dic)
                return True
            elif(choice == 1):
                obj.two_point_crossover(individual_dic)
                return True
            elif(choice == 2):
                obj.uniform_point_crossover(individual_dic)
                return True
            elif(choice == 3):
                obj.partialy_matched_crossover(individual_dic)
                return True
            elif(choice == 4):
                obj.cycle_crossover(individual_dic)
                return True
            else:
                return False
        else:
            print('Your choice is Out of Range. Please choose from list')
            return True
        
    def one_point_crossover(individual_dic):
        first_parent = input('Select the first parent:')
        second_parent = input('Select the second parent:')
        cross_over_point = int(input('Select the crossover point:'))
        first_chromosome = individual_dic.get(first_parent)
        second_chromosome = individual_dic.get(second_parent)
        print('The first chrosome', first_chromosome)
        print('The second chrosome', second_chromosome)
        l, r = str(first_chromosome)[:cross_over_point], str(first_chromosome)[cross_over_point:]
        l2, r2 = str(second_chromosome)[:cross_over_point], str(second_chromosome)[cross_over_point:]
        print('first crossover', l+r2)
        print('second crossover', l2 + r)
        
    def two_point_crossover(individual_dic):
        first_parent = input('Select the first parent:')
        second_parent = input('Select the second parent:')
        first_cross_over_point = int(input('Select the first crossover point:'))
        second_cross_over_poing = int(input('Select the second crossover point:'))
        
        first_chromosome = individual_dic.get(first_parent)
        second_chromosome = individual_dic.get(second_parent)
        print('The first chrosome', first_chromosome)
        print('The second chrosome', second_chromosome)
        l, m, r = str(first_chromosome)[:first_cross_over_point], str(first_chromosome)[first_cross_over_point:second_cross_over_poing], str(first_chromosome)[second_cross_over_poing:]
        l2, m2, r2 = str(second_chromosome)[:first_cross_over_point], str(second_chromosome)[first_cross_over_point:second_cross_over_poing], str(second_chromosome)[second_cross_over_poing:]
        print('first crossover', l+m2+r)
        print('second crossover', l2 + m + r2)
        
    def cross_over_evaluation(sorted_list, individual_dic):
        running = True
        while running:
            print('Select type of crossover to perform:')
            print(' One point crossover : 0\n Two point crossover : 1\n Uniform crossover : 2\n Partially matched crossover : 3\n Cycle crossover : 4\n Exit from crossover : 5')
            choice = int(input('To calculate, choose the corresponding number:'))
            #switch to the corresponding choice
            status = obj.switcher(choice, sorted_list, individual_dic)
            running = status
obj = GeneticAlgorithm

#individual_no = 4
#gene_no = 6

individual_no = int(input('Enter number of Individual:'))
gene_no = int(input('Enter number of Genes:'))
obj.individual_with_gene_no(individual_no, gene_no)
