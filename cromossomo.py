import random
import config
import json


class Cromossomo:
    '''Classe que representa um indíviduo (cromossomo), sua composição de genes e suas características'''

    def __init__(self):
        self.weight = 0  # peso do cromossomo (pela soma dos genes)
        self.value = 0  # valor do cromossomo (pela soma dos genes)
        self.compositionSize = 0 #config.composition_size  # número de genes do cromossomo
        # inicializa todos os genes com 0
        self.composition = [] # [0 for i in range(self.compositionSize)]
        # atributo que define se cromosso atende critério de aceitação (fitness)
        self.fitness = False
        # atributo informativo para saber o percentual de ocupação em relação ao limite de peso
        self.usedWeightPercent = 0
        self.mutateMethod = config.mutateMethod  # método de mutação de genes

        # dados dos itens a serem avaliados para a mochila
        self.file = config.dataset
        # valor dos itens da mochila (respectivo ao peso)
        self.available_itens_value = []
        # peso dos itens da mochila (respectivo ao valor)
        self.available_itens_weight = []
        # capacidade máxima de peso para a mochila, em kg
        self.knapsackCapacity = 0
        # realiza a leitura do arquivo de dataset
        self.readJson()

    def initialize(self):
        '''Define 0s e 1s aleatórios para compor o cromossomo'''
        for i in range(self.compositionSize):
            self.composition[i] = random.randint(0, 1)
        self.evaluate_fitness()  # atualiza características do cromossomo

    def evaluate_fitness(self):
        '''Calcula e atualiza  as características do cromossomo'''
        self.value = 0
        self.weight = 0
        for i in range(self.compositionSize):
            # cada gene ativo '1' indica que peso e valor desse gene são somados no cromossomo
            if (self.composition[i] == 1):
                self.value += self.available_itens_value[i]
                self.weight += self.available_itens_weight[i]

        # calcula o percentual do peso que o cromossomo está usando em relação ao limite (carater informativo)
        # e se ultrapassar a capacidade da mochila, zera seu valor
        self.usedWeightPercent = (self.weight * 100) / \
            (self.knapsackCapacity)
        if (self.usedWeightPercent > 100):
            self.usedWeightPercent = 0
        self.usedWeightPercent = int(self.usedWeightPercent)

        # avalia se o cromossomo atende as expectativas de fitness (se não ultrapassa capacidade da mochila)
        if (self.weight <= self.knapsackCapacity):
            self.fitness = True
        else:
            self.fitness = False

    def mutate(self):
        '''Método que realiza a mutação de um cromossomo, que pode ser feito de duas formas:
        - fix: define um grupo fixo de genes que sofrem mutação
        - random: define aleatoriamente quais genes sofrem mutação
        - none: não realiza nenhuma mutação'''
        if (self.mutateMethod == "fix"):
            self.fix_mutate()
        elif (self.mutateMethod == "random"):
            self.rand_mutate()
        self.evaluate_fitness()  # atualiza características do cromossomo

    def fix_mutate(self):
        '''Faz a mutação dos genes centrais do cromossomo, assumindo valores aleatórios'''
        l = self.compositionSize//2
        i = l - (l//2)
        f = i + l
        for m in range(i, f):
            self.locus_change(m)

    def rand_mutate(self):
        '''Faz a mutação de um número aleatório de genes, com valores aleatórios'''
        r = random.randint(0, self.compositionSize)
        for i in range(0, r):
            m = random.randint(0, self.compositionSize-1)
            self.locus_change(m)

    def locus_change(self, m):
        '''Faz a mutação de um gene em específico para um valor aleatório'''
        self.composition[m] = random.randint(0, 1)

    def readJson(self):
        with open(f'datasets/{self.file}.json') as json_file:
            data = json.load(json_file)
        self.knapsackCapacity = data["capacity"]
        self.available_itens_value = data["values"]
        self.available_itens_weight = data["weights"]
        self.compositionSize = len(data["values"])
        self.composition = [0 for i in range(self.compositionSize)]
