import random
from cromossomo import Cromossomo
from population import Population
import config

print("Problema da Mochila usando Algoritmo Genético")

chronology = []

population = Population()
population.initialize()
population.evaluate()

print(f"Initial Population")
population.print()

chronology.append(population)

for i in range(config.generations-1):

    newPop = Population()
    newPop.procreate( chronology[-1] )
    newPop.evaluate()

    print(f"Population {i}")
    newPop.print()

    chronology.append(newPop)

print("fim")