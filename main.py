import random
from cromossomo import Cromossomo

print("Problema da Mochila usando Algoritmo Genético")

available_itens_weight = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
available_itens_value  = [3, 2, 1, 9,  4,  3,  5,  3,  1,  2]

population = []
knapsackCapacity = 30

#População inicial:
# uma população composta de n indivíduos (cromossomos), gerada aleatoriamente para iniciar
# o processo de busca por soluções para o problema em questão

for i in range(10):
    cromossomo = Cromossomo()
    cromossomo.initialize()
    population.append(cromossomo)

print("fim")