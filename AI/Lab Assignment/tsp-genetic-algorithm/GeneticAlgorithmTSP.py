import numpy as np
import operator
import Graph2
import math

class GeneticAlgorithmTSP:
    def __init__(self, generations=100, population_size=10, tournamentSize=4, mutationRate=0.1, elitismRate=0.1):

        # assinging values
        self.generations = generations
        self.population_size = population_size
        self.tournamentSize = tournamentSize
        self.mutationRate = mutationRate
        self.elitismRate = elitismRate
    
    def optimize(self, graph):
        population = self.__makePopulation(graph.getVertices())
        elitismOffset = math.ceil(self.population_size*self.elitismRate)
        # In Genetic Algorithms sometimes the fittest genomes from the current generation are passed directly to the next, contesting with the offsprings and crossover to - potentially - fitter solutions.
        if (elitismOffset > self.population_size):
            raise ValueError('Elitism Rate must be in [0,1].')
        
        print ('Optimizing TSP Route for Graph:\n{0}'.format(graph))

        for generation in range(self.generations):
            print ('\nGeneration: {0}'.format(generation + 1))
            print ('Population: {0}'.format(population))
            
            newPopulation = []            
            fitness = self.__computeFitness(graph, population)
            print ('Fitness:    {0}'.format(fitness))
            fittest = np.argmin(fitness)

            print ('Fittest Route: {0} ({1})'.format(population[fittest], fitness[fittest]))
            
            if elitismOffset:
                elites = np.array(fitness).argsort()[:elitismOffset]
                [newPopulation.append(population[i]) for i in elites]
            for gen in range(elitismOffset, self.population_size):
                parent1 = self.__tournamentSelection(graph, population)
                parent2 = self.__tournamentSelection(graph, population)
                offspring = self.__crossover(parent1, parent2)
                newPopulation.append(offspring)
                # print ('\nParent 1: {0}'.format(parent1))
                # print ('Parent 2: {0}'.format(parent2))
                # print ('Offspring: {0}\n'.format(offspring))
            for gen in range(elitismOffset, self.population_size):
                newPopulation[gen] = self.__mutate(newPopulation[gen])
    
            population = newPopulation

            if self.__converged(population):
                print ('\nConverged to a local minima.', end='')
                break

        # The Algorithm stops if: 1)All genomes in the population are the same or 2) Reached the max. Generation limit


        return (population[fittest], fitness[fittest])


    # In this problem the population is a list of strings (genomes) that each letter (allele) is a vertex of the given graph.
    def __makePopulation(self, graph_nodes):
        return [''.join(v for v in np.random.permutation(graph_nodes)) for i in range(self.population_size)]
    

    # It's the measure used to compare genomes to each other. For this problem a fitness function (and the one we use in this implementation) is the sum of the edge's weights through the graph for a certain path - encoded in the genome.
    def __computeFitness(self, graph, population):
        return [graph.getPathCost(path) for path in population]


    # Each generation must have N genomes at a time. To achieve evolution we select some at the genomes to Crossover them and produce Offsprings that will be part of the new population. 
    def __tournamentSelection(self, graph, population):
        tournament_contestants = np.random.choice(population, size=self.tournamentSize)
        # print (tournament_contestants)
        tournament_contestants_fitness = self.__computeFitness(graph, tournament_contestants)
        return tournament_contestants[np.argmin(tournament_contestants_fitness)]
    
    #  we have our parent genomes from the Selection procedure, now we crossover them to produce - potentially - fitter offsprings. 
    def __crossover(self, parent1, parent2):

        # Select a subset from the first parent.
        # Add that subset to the offspring.
        # Any missing values are then added to the offspring from  the second parent in order that they are found.


        offspring = ['' for allele in range(len(parent1))]
        index_low, index_high = self.__computeLowHighIndexes(parent1)
        
        offspring[index_low:index_high+1] = list(parent1)[index_low:index_high+1]
        offspring_available_index = list(range(0, index_low)) + list(range(index_high+1, len(parent1)))        
        for allele in parent2:
            if '' not in offspring:
                break
            if allele not in offspring:
                offspring[offspring_available_index.pop(0)] = allele
        return ''.join(v for v in offspring) 


    # After making the offsprings of the next generation, to finalize the creation of the new population we must mutate the genomes.
    def __mutate(self, genome):
        if np.random.random() < self.mutationRate:
            index_low, index_high = self.__computeLowHighIndexes(genome)
            return self.__swap(index_low, index_high, genome)
        else:
            return genome


    def __computeLowHighIndexes(self, string):
        index_low = np.random.randint(0, len(string)-1)
        index_high = np.random.randint(index_low+1, len(string))
        while index_high - index_low > math.ceil(len(string)//2):
            try:
                index_low = np.random.randint(0, len(string))
                index_high = np.random.randint(index_low+1, len(string))
            except ValueError:
                pass
        return (index_low, index_high)


    def __swap(self, index_low, index_high, string):
        string = list(string)
        string[index_low], string[index_high] = string[index_high], string[index_low]
        return ''.join(string)


    def __converged(self, population):
        return all(genome == population[0] for genome in population)


if __name__ == '__main__':
    graph = Graph2.Graph()

    # using the graph data structure to setup the distances and places according to the question
    graph.setAdjacent('0', '1', 1)
    graph.setAdjacent('0', '2', 3)
    graph.setAdjacent('0', '3', 4)
    graph.setAdjacent('0', '4', 5)
    graph.setAdjacent('1', '2', 1)
    graph.setAdjacent('1', '3', 4)
    graph.setAdjacent('1', '4', 8)
    graph.setAdjacent('2', '3', 5)
    graph.setAdjacent('2', '4', 1)
    graph.setAdjacent('3', '4', 2)


    ga_tsp = GeneticAlgorithmTSP(generations=20, population_size=7, tournamentSize=2, mutationRate=0.2, elitismRate=0.1)
    
    optimal_path, path_cost = ga_tsp.optimize(graph)
    print ('\nPath: {0}, Cost: {1}'.format(optimal_path, path_cost))
