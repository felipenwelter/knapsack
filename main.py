import random

print("Problema da Mochila usando Algoritmo Genético")

population = []

#População inicial:
# uma população composta de n indivíduos (cromossomos), gerada aleatoriamente para iniciar
# o processo de busca por soluções para o problema em questão
for i in range(20):
    weight = random.randint(1,30)
    value = random.randint(1,10)
    population.append([weight,value])

print(population)