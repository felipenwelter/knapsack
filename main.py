import random
from cromossomo import Cromossomo
from population import Population

print("Problema da Mochila usando Algoritmo Genético")

available_itens_weight = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
available_itens_value  = [3, 2, 1, 9,  4,  3,  5,  3,  1,  2]

population = []
knapsackCapacity = 30

population = Population()
population.initialize()
population.evaluate()

population.print()




print("fim")