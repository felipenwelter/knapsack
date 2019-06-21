import random
import numpy as np
from cromossomo import Cromossomo

print("Problema da Mochila usando Algoritmo Genético")

available_itens_weight = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
available_itens_value  = [3, 2, 1, 9,  4,  3,  5,  3,  1,  2]

population = []
knapsackCapacity = 30

class Population:

    def __init__(self):
        self.cromossomos = []
        self.size = 10
        self.avg = 0

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
            c.evaluate_fitness(knapsackCapacity)
            self.avg += c.weight
        self.avg = self.avg/self.size

    def print(self):
        for c in self.cromossomos:
            print(f"composition {c.composition} weight {c.weight} value {c.value} fitness {c.fit}")
        print(f" population weight average is {self.avg} kg")

    def procreate(self,ancestral):
        for i in range(self.size):
            p1, p2 = self.selectParents(ancestral)
            new_cromossomo = self.crossover(p1,p2)
            self.cromossomos.append(new_cromossomo)

    def selectParents(self,ancestral):
        r = random.randint(0,ancestral.size-1)
        p1 = ancestral.cromossomos[r]
        r = random.randint(0,ancestral.size-1)
        p2 = ancestral.cromossomos[r]
        return p1, p2

    def crossover(self,p1,p2):
        #faz crossover unindo a primeira metade de genes do primeiro progenitor
        #com a segunda meteade de genes do segundo progenitor
        half = int(p1.compositionSize/2)
        new_composition = p1.composition[:half] + p2.composition[half:]
        c = Cromossomo()
        c.composition = new_composition
        c.calc()
        return c