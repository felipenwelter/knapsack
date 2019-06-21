import random
from cromossomo import Cromossomo
from population import Population
import config

print("Problema da Mochila usando Algoritmo Genético")

population = Population()
population.initialize()
population.evaluate()

population.print()

newPop = Population()
newPop.procreate(population)
newPop.evaluate()

newPop.print()

print("fim")