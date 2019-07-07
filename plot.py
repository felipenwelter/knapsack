# ESTÁ CONFIGURADO PARA TRABALHAR COM ATÉ 50 POPULAÇÕES

import matplotlib.pyplot as plt
import numpy as np
import json
import config
from population import sortPopulation

# segmentacao dos subgraficos: número de linhas e colunas
subplot_config = [
    [0, 0], [1, 1], [1, 2], [1, 3], [2, 2],
    [1, 5], [2, 3], [2, 4], [2, 4], [3, 3],
    [2, 5], [2, 6], [3, 4], [3, 5], [3, 5],
    [3, 5], [4, 4], [3, 6], [3, 6], [3, 7],
    [3, 7], [3, 7], [3, 8], [3, 8], [3, 8],
    [3, 9], [3, 9], [3, 9], [3, 10], [3, 10],
    [3, 10], [4, 8], [4, 8], [4, 9], [4, 9],
    [4, 9], [4, 9], [4, 10], [4, 10], [4, 10],
    [4, 10], [5, 9], [5, 9], [5, 9], [5, 9],
    [5, 9], [5, 10], [5, 10], [5, 10], [5, 10], [5, 10]]


def shouldPrint(cromossomo, population):
    best = sortPopulation(population.cromossomos)
    pos = best.index(cromossomo)
    if config.procreateMethod == "all_elite" or config.procreateMethod == "random":
        return best[pos].fitness
    elif config.procreateMethod == "first_elite":
        return (pos == 0) and best[pos].fitness


def plot(chronology):

    with open(f'datasets/{config.dataset}.json') as json_file:
        data = json.load(json_file)
    knapsackCapacity = data["capacity"]
    available_itens_weight = data["weights"]

    # define limites x e y do grafico
    x_limit = (np.sum(available_itens_weight) + 10)
    y_limit = knapsackCapacity + 5

    index = 1

    # para cada populacao
    for p in chronology:

        x = []
        y = []

        # para cada cromossomo na populacao
        for c in p.cromossomos:

            if not shouldPrint(c, p):
                # imprime todos os cromossomos, exceto os que atendem fitness
                x.append(c.weight)
                y.append(c.value)

        # divide número de linhas e colunas para indexar os subgraficos
        plt.subplot(subplot_config[len(chronology)][0],
                    subplot_config[len(chronology)][1], index)

        # imprime linha fixa do limite da mochila
        plt.plot(np.full(y_limit+3, knapsackCapacity),
                 np.arange(y_limit+3))

        # configura limites do grafico
        plt.axis([0, x_limit, 0, y_limit])

        # define titulo do grafico (número da população)
        plt.title(index-1, fontsize=8)

        # imprime todos os valores de x e y
        plt.plot(x, y, 'r.')

        # imprime em destaque os melhores cromossomos (baseado no fitness)
        for c in p.cromossomos:
            if shouldPrint(c, p):
                # imprime todos os cromossomos que atendem fitness
                plt.plot(c.weight, c.value, 'b.')

        index += 1

    fig = plt.gcf()
    fig.canvas.set_window_title('Knacksack Problem - UDESC 2019')
    fig.suptitle(
        f"Knapsack Problem\n procreate: {config.procreateMethod} | mutate: {config.mutateMethod} | population: {config.generations} | individuals: {config.population_size}", fontsize=9)

    plt.rc('xtick', labelsize=10)
    plt.rc('ytick', labelsize=10)

    # apresenta o graficos
    #plt.show()
