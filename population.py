import random
import time
import numpy as np
import operator
import config
from cromossomo import Cromossomo


def sortPopulation(newList: list):
    '''ordena primeiro os valores fitness = true, depois value, depois weight, por exemplo:
    true/19/29 - true/19/28 - true/18/30 - true 18/25 - true/18/25 - false/26/50'''
    sortedList = sorted(
        newList, key=operator.attrgetter('weight'), reverse=True)
    sortedList = sorted(
        sortedList, key=operator.attrgetter('value'), reverse=True)
    sortedList = sorted(
        sortedList, key=operator.attrgetter("fitness"), reverse=True)
    return sortedList


class Population:
    '''Classe que representa a população de uma geração com um determinado número de indivíduos (cromossomos)'''

    def __init__(self):
        self.cromossomos = []  # armazena os indivíduos (classe cromossomo)
        self.size = config.population_size  # define o número de invíduos da população
        # a média de peso dos indivíduos da população (informativo)
        self.weightAverage = 0
        # método de procriação (geração de nova população)
        self.procreateMethod = config.procreateMethod

    def initialize(self):
        '''inicializa a população de cromossomos com valores aleatórios'''
        for i in range(self.size):
            cromossomo = Cromossomo()
            cromossomo.initialize()
            self.cromossomos.append(cromossomo)

    def evaluate(self):
        '''Avalia cada cromossomo individualmente e recalcula seus atributos. Também realiza 
        cálculos relativos a própria população, como por exemplo a média de peso.'''
        self.weightAverage = 0
        for c in self.cromossomos:
            c.evaluate_fitness()
            self.weightAverage += c.weight
        self.weightAverage = round(self.weightAverage/self.size, 2)

    def print(self):
        '''Imprime em tela cada cromossomo da população e suas características principais '''
        # ordena pelo maior valor
        sortedList = sortPopulation(self.cromossomos)
        for c in sortedList:
            print(
                f"composition {c.composition} weight {c.weight} | value {c.value} | %limit Weight {c.usedWeightPercent} | fitness {c.fitness}")
        print(f" population weight average is {self.weightAverage} kg")

    def procreate(self, ancestral: object):
        '''Geração de uma nova população a partir de uma população ancestral. Permite três formas diferentes:
        - random: a seleção dos progenitores é feita de forma aleatória
        - all_elite: todos os elementos que atendem ao critério fitness são copiados para a próxima geração
        - first_elite: apenas o elemento mais próximo ao critério fitness é copiado para a próxima geração
        em seguida é realizado o processo de crossover e mutação dos novos cromossomos, em casos específicos.'''

        if (self.procreateMethod == "random"):
            for i in range(self.size):
                # não replica nenhum item da população ancestral para a nova população
                p1, p2 = self.selectParents(ancestral.cromossomos)
                new_cromossomo = self.crossover(p1, p2)
                new_cromossomo.mutate()
                self.cromossomos.append(new_cromossomo)

        elif (self.procreateMethod == "all_elite"):
            # replica para a nova população todos os cromossomos que atendem criterio de fitness
            selected = []
            newList = sortPopulation(ancestral.cromossomos)
            for i in range(self.size):
                if (newList[i].fitness == True):
                    self.cromossomos.append(newList[i])
                else:
                    break

            # completa a população fazendo crossover dos cromossomos selecionados
            missingCromossomos = len(
                ancestral.cromossomos) - len(self.cromossomos)
            for i in range(missingCromossomos):
                p1, p2 = self.selectParents(selected if len(
                    selected) > 0 else ancestral.cromossomos)
                new_cromossomo = self.crossover(p1, p2)
                new_cromossomo.mutate()  # mutação do novo cromossomo
                self.cromossomos.append(new_cromossomo)

        elif (self.procreateMethod == "first_elite"):
            # replica para a nova população somente o melhor cromossomo que atende ao criterio de fitness
            selected = []
            newList = sortPopulation(ancestral.cromossomos)
            if (newList[0].fitness == True):
                selected.append(newList[0])
                self.cromossomos.append(newList[0])

            # completa a população fazendo crossover dos cromossomos selecionados
            missingCromossomos = len(
                ancestral.cromossomos) - len(self.cromossomos)
            for i in range(missingCromossomos):
                p1, p2 = self.selectParents(selected if len(
                    selected) > 0 else ancestral.cromossomos)
                new_cromossomo = self.crossover(p1, p2)
                new_cromossomo.mutate()  # mutação do novo cromossomo
                self.cromossomos.append(new_cromossomo)

    def selectParents(self, cromossomoList: list) -> tuple: 
        '''Seleciona os pais para realizar o cruzamento. Busca os pais a partir de uma lista
        restrita de cromossomos de uma população anterior enviada como parâmetro.'''
        limit = len(cromossomoList)
        r = random.randint(0, limit-1)
        p1 = cromossomoList[r]
        s = random.randint(0, limit-1)
        p2 = cromossomoList[s]
        return p1, p2

    def crossover(self, p1: object, p2: object) -> object:
        '''Faz cruzamento (crossover) unindo a primeira metade de genes do primeiro progenitor
        com a segunda meteade de genes do segundo progenitor'''
        half = int(p1.compositionSize/2)
        new_composition = p1.composition[:half] + p2.composition[half:]
        c = Cromossomo()
        c.composition = new_composition
        c.evaluate_fitness()  # atualiza características do cromossomo
        return c
