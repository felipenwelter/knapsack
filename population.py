import random
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
            population.append(cromossomo)

    def evaluate(self):
        self.avg = 0
        for c in population:
            c.evaluate_fitness(knapsackCapacity)
            self.avg += c.weight
        self.avg = self.avg/self.size

    def print(self):
        for c in population:
            print(f"composition {c.composition} weight {c.weight} value {c.value} fitness {c.fit}")
        print(f" population weight average is {self.avg} kg")
