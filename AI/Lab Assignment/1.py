import random
import numpy as np

class individual:
    gnome = 0
    fitness = 0

V = 5
GENES = "ABCDE"
START = 0
POP_SIZE = 10
INT_MAX = 9999999

def rand_num(start, end):
    return np.random.rand(start,end)

def repeat (s,ch):
    for i in range(s.size):
        if s[i] == ch:
            return True
    return False

def mutatedDene(gnome):
    while True:
        r = rand_num(1,V)
        r1 = rand_num(1,V)
        if r1!=r:
            temp = gnome[r]
            gnome[r] = gnome[r1]
            gnome[r1] = temp
            break
    return gnome

def createGnome():
    gnome = "0"
    while True:
        if(len(gnome) == V):
            gnome += gnome[0]
            break

        temp = rand_num(1,V)
        if repeat(gnome, chr(temp + 48)):
            gnome+= chr(temp + 48)

    return gnome

def cal_fitness(gnome):
    MAP[V][V] =  [ [ 0, 2, INT_MAX, 12, 5 ], 
                      [ 2, 0, 4, 8, INT_MAX ], 
                      [ INT_MAX, 4, 0, 3, 3 ], 
                      [ 12, 8, 3, 0, 10 ], 
                      [ 5, INT_MAX, 3, 10, 0 ] ]

    f = 0 
    for i in range(len(gnome)):
        if MAP[gnome[i] - 48][gnome[i+1]-48] == INT_MAX:
            return INT_MAX
        f+= MAP[gnome[i] - 48][gnome[i+1] - 48]
    return f

def cooldown(temp):
    return (90*temp)/100

def lessthan(t1,t2):
    return t1.fitness < t2.fitness

def TSPUtil(MAP):
    gen = 1
    gen_thres = 5
    population = []
    temp = individual()

    for i in range(POP_SIZE):
        temp.gnome = createGnome()
        temp.fitness = cal_fitness(temp.gnome)
        population.append(temp)

    print("\n intitial population: \n Gnome Fitness value \n")

    for i in range(POP_SIZE):
        print(population[i].gnome + " " + population[i].fitness)
        print("\n")

    found = False
    temperature = 1000

    while temperature > 1000 and gen <= gen_thres:
        population.sort(key=sortfn, reverse=True)
        print("Current temperature " + temperature)
        newPopulation = []
        
        for i in range(POP_SIZE):
             p1 = population[i]
             new_gnome = individual()

             while True:
                 new_g = mutatedDene(p1.gnome)
                 new_gnome.gnome = new_g
                 new_gnome.fitness = cal_fitness(new_gnome.gnome)

                 if new_gnome.fitness <= population[i].fitness:
                     newPopulation.append(new_gnome)
                     break
                 else:
                     prob = pow(2.7,-1*(new_gnome.fitness - population[i].fitness)/temperature)
                     if prob > 0.5:
                         newPopulation.append(new_gnome)
                         break

    temperature = cooldown(temperature)
    population = newPopulation
    print("Generation " + gen + " \n")
    print("GNOME  Fitness Value\n")

    for i in range(POP_SIZE):
        print(population[i].gnome + " " + population[i].fitness + "\n")
    
    gen+=1

def sortfn(e):
    return e.begin() - e.end()

if __name__ == "__main__":
    MAP = [ [ 0, 2, INT_MAX, 12, 5 ], 
                [ 2, 0, 4, 8, INT_MAX ], 
                [ INT_MAX, 4, 0, 3, 3 ], 
                [ 12, 8, 3, 0, 10 ], 
                [ 5, INT_MAX, 3, 10, 0 ] ]
    TSPUtil(MAP)