import random
import numpy as np
from cromossomo import Cromossomo
import config
import operator

print("Problema da Mochila usando Algoritmo Genético")

def sortPopulation(newList):
    #ordena primeiro os valores fitness = true, depois value, depois weight, por exemplo:
    # true/19/29 - true/19/28 - true/18/30 - true 18/25 - true/18/25 - false/26/50
    sortedList = sorted(newList, key=operator.attrgetter('weight'),reverse=True)
    sortedList = sorted(sortedList, key=operator.attrgetter('value'), reverse=True)
    sortedList = sorted(sortedList, key=operator.attrgetter("fitness"),reverse=True)
    return sortedList


class Population:

    def __init__(self):
        self.cromossomos = []
        self.size = config.population_size
        self.avg = 0
        self.procreateMethod = "first_elite"

    #População inicial:
    # uma população composta de n indivíduos (cromossomos), gerada aleatoriamente para iniciar
    # o processo de busca por soluções para o problema em questão
    
    def initialize(self):
        for i in range(self.size):
            cromossomo = Cromossomo()
            cromossomo.initialize()
            self.cromossomos.append(cromossomo)

    def evaluate(self):
        self.avg = 0
        for c in self.cromossomos:
            c.evaluate_fitness()
            self.avg += c.weight
        self.avg = round(self.avg/self.size,2)

    def print(self):
        #ordena pelo maior valor
        sortedList = sortPopulation(self.cromossomos)
        for c in sortedList:
            print(f"composition {c.composition} weight {c.weight} | value {c.value} | %limit Weight {c.usedWeightPercent} | fitness {c.fitness}")
        #print(f" population weight average is {self.avg} kg")

    def procreate(self,ancestral):

        if (self.procreateMethod == "random"):
            for i in range(self.size):
                p1, p2 = self.selectParents(ancestral.cromossomos)
                new_cromossomo = self.crossover(p1,p2)
                self.cromossomos.append(new_cromossomo)

        elif (self.procreateMethod == "all_elite"):
            #seleciona somente itens que atendem criterio de fitness
            selected = []
            newList = sortPopulation(ancestral.cromossomos)
            for i in range(self.size):
                if (newList[i].fitness == True):
                    self.cromossomos.append(newList[i])
                else:
                    break

            missingCromossomos = len(ancestral.cromossomos) - len(self.cromossomos)
            for i in range( missingCromossomos ):
                p1, p2 = self.selectParents(selected if len(selected) > 0 else ancestral.cromossomos )
                new_cromossomo = self.crossover(p1,p2)
                new_cromossomo.mutate()
                self.cromossomos.append(new_cromossomo)

        elif (self.procreateMethod == "first_elite"):
            #seleciona somente o melhor item que atende ao criterio de fitness
            selected = []
            newList = sortPopulation(ancestral.cromossomos)
            if (newList[0].fitness == True):
                selected.append(newList[0])
                self.cromossomos.append(newList[0])

            missingCromossomos = len(ancestral.cromossomos) - len(self.cromossomos)
            for i in range( missingCromossomos ):
                p1, p2 = self.selectParents(selected if len(selected) > 0 else ancestral.cromossomos )
                new_cromossomo = self.crossover(p1,p2)
                new_cromossomo.mutate()
                self.cromossomos.append(new_cromossomo)

    def selectParents(self,cromossomoList):
        limit = self.size if len(cromossomoList) == 0 else len(cromossomoList)
        r = random.randint(0,limit-1)
        p1 = cromossomoList[r]
        r = random.randint(0,limit-1)
        p2 = cromossomoList[r]
        return p1, p2

    def customsort(e):
        return e.weight


    def crossover(self,p1,p2):
        #faz crossover unindo a primeira metade de genes do primeiro progenitor
        #com a segunda meteade de genes do segundo progenitor
        half = int(p1.compositionSize/2)
        new_composition = p1.composition[:half] + p2.composition[half:]
        c = Cromossomo()
        c.composition = new_composition
        c.evaluate_fitness()
        return c
