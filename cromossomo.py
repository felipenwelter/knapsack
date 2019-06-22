import random
import config

class Cromossomo:
    '''Classe que representa um indíviduo (cromossomo), sua composição de genes e suas características'''

    def __init__(self):
        self.weight = 0 #peso do cromossomo (pela soma dos genes)
        self.value = 0 #valor do cromossomo (pela soma dos genes)
        self.compositionSize = config.composition_size #número de genes do cromossomo
        self.composition = [0 for i in range(self.compositionSize)] #inicializa todos os genes com 0
        self.fitness = False #atributo que define se cromosso atende critério de aceitação (fitness)
        self.usedWeightPercent = 0 #atributo informativo para saber o percentual de ocupação em relação ao limite de peso
        self.mutateMethod = config.mutateMethod #método de mutação de genes
    
    def initialize(self):
        '''Define 0s e 1s aleatórios para compor o cromossomo'''
        for i in range(self.compositionSize):
            self.composition[i] = random.randint(0,1)
        self.evaluate_fitness() #atualiza características do cromossomo
    
    def evaluate_fitness(self):
        '''Calcula e atualiza  as características do cromossomo'''
        self.value = 0
        self.weight = 0
        for i in range(self.compositionSize):
            #cada gene ativo '1' indica que peso e valor desse gene são somados no cromossomo
            if (self.composition[i] == 1):
                self.value += config.available_itens_value[i]
                self.weight += config.available_itens_weight[i]

        #calcula o percentual do peso que o cromossomo está usando em relação ao limite (carater informativo)
        #e se ultrapassar a capacidade da mochila, zera seu valor
        self.usedWeightPercent = (self.weight * 100 ) / (config.knapsackCapacity)
        if (self.usedWeightPercent > 100):
            self.usedWeightPercent = 0
        self.usedWeightPercent = int(self.usedWeightPercent)

        #avalia se o cromossomo atende as expectativas de fitness (se não ultrapassa capacidade da mochila)
        if (self.weight <= config.knapsackCapacity):
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
        self.evaluate_fitness() #atualiza características do cromossomo

    def fix_mutate(self):
        '''Faz a mutação dos genes centrais do cromossomo, assumindo valores aleatórios'''
        l = self.compositionSize//2
        i = l - (l//2)
        f = i + l
        for m in range(i,f):
            self.locus_change(m)

    def rand_mutate(self):
        '''Faz a mutação de um número aleatório de genes, com valores aleatórios'''
        r = random.randint(0,self.compositionSize)
        for i in range(0,r):
            m = random.randint(0,self.compositionSize-1)
            self.locus_change(m)   

    def locus_change(self,m):
        '''Faz a mutação de um gene em específico para um valor aleatório'''
        self.composition[m] = random.randint(0,1)