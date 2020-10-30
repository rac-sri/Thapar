import random
import numpy as np
from collections import namedtuple

individual = new namedtuple("individual","gnome fitness")

def rand_num (self, start, end):
    return np.random.rand(start,end)

def repeat ( s , ch ):
    for i in range(s.size):
        if s[i] == ch
            return True
    return False

def mutatedDene(string gnome):
    while True
        r = rand_num(1,V)
        r1 = rand_num(1,V)
        if r1!=r:
            char temp = gnome[r]
            gnome[r] = gnome[r1]
            gnome[r1] = temp
            break
    return gnome

def createGnome():
    gnome = "0"
    while True
        if(gnome.size() == v):
            gnome += gnome[0]
            break

        temp = rand_num(1,V)
        if repeat(gnome, chr(temp + 48))

    return gnome

def cal_fitness(gnome):
    map[V][V] =  [ [ 0, 2, INT_MAX, 12, 5 ], 
                      [ 2, 0, 4, 8, INT_MAX ], 
                      [ INT_MAX, 4, 0, 3, 3 ], 
                      [ 12, 8, 3, 0, 10 ], 
                      [ 5, INT_MAX, 3, 10, 0 ] ]

    f = 0 
    for i in range[gnome.size()]:
        if map[gnome[i] - 48][gnome[i+1]-48] == IN:
            return INT_MAX
        f+= map[gnome[i] - 48][gnome[i+1] - 48]
    return f

def cooldown(temp):
    return (90*temp)/100

def lessthan(individual t1, individial t2):
    return t1.fitness < t2.fitness

def TSPUtil(map[V][V]):
    gen = 1
    gen_thres = 5
    population = []
    temp

    for i in range[POP_SIZE]:
        temp.gnome = create_gnome()
        temp.fitness = cal_fitness(temp.gnome)
        population.append(temp)

    print("\n intitial population: \n Gnome Fitness value \n")

    for i in rnage[POP_SIZE]:
        print(population[i].gnome + " " + population[i].fitness)
        print("\n")

    found = False
    temperature = 1000

    while temperature > 1000 and gen <= gen_thres:
        population.sort(key=sortfn, reverse=true)
        print("Current temperature " + temperature)
        newPopulation = []

        for i in range[POP_SIZE]:
             p1 = population[i]

             while True:
                 new_g = mutatedDene(p1.gnome)
                 new_gnome.gnome = new_g
                 new_gnome.fitness = cal_fitness(new_gnome.gnome)

                 if new_gnome.fitness <= population[i].fitness:
                     newPopulation.append(new_gnome)
                     break
                 else:
                     prob = pow(2.7,-1*((float)new_gnome.fitness - population[i].fitness)/temperature)
                     if prob > 0.5:
                         newPopulation.append(new_gnome)
                         break

    temperature = cooldown[temperature]
    population = newPopulation
    print("Generation " + gen + " \n")
    print("GNOME  Fitness Value\n")

    for i in range[POP_SIZE]:
        print(population[i].gnome + " " + population[i].fitness + "\n")
    
    gen+=1

def sortfn(e):
    return e.begin() - e.end()

if __init__="__main__":
    map[V][V] = [ [ 0, 2, INT_MAX, 12, 5 ], 
                      [ 2, 0, 4, 8, INT_MAX ], 
                      [ INT_MAX, 4, 0, 3, 3 ], 
                      [ 12, 8, 3, 0, 10 ], 
                      [ 5, INT_MAX, 3, 10, 0 ] ]
    TPSUtil(map)