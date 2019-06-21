import random
import config

class Cromossomo:

    def __init__(self):
        self.weight = 0
        self.value = 0
        self.compositionSize = config.composition_size
        self.composition = [0 for i in range(self.compositionSize)]
        self.fitness = False
        self.usedWeightPercent = 0
        self.mutateMethod = "random"
    
    def initialize(self):
        # define 0s e 1s aleatorios para compor o cromossomo
        for i in range(self.compositionSize):
            self.composition[i] = random.randint(0,1)
        self.evaluate_fitness()
    
    def evaluate_fitness(self):
        #calcula as características do cromossomo
        self.value = 0
        self.weight = 0
        for i in range(self.compositionSize):
            if (self.composition[i] == 1):
                self.value += config.available_itens_value[i]
                self.weight += config.available_itens_weight[i]

        # primeiro calcula o percentual do peso está usando (carater informativo)
        self.usedWeightPercent = (self.weight * 100 ) / (config.knapsackCapacity)
        if (self.usedWeightPercent > 100):
            self.usedWeightPercent = 0
        self.usedWeightPercent = int(self.usedWeightPercent)

        #avalia se o cromossomo atende as expectativas de fitness
        if (self.weight <= config.knapsackCapacity):
            self.fitness = True
        else:
            self.fitness = False

    def mutate(self):
        if (self.mutateMethod == "fix"):
            self.fix_mutate()
        elif (self.mutateMethod == "random"):
            self.rand_mutate()
        self.evaluate_fitness() 

    def fix_mutate(self):
        l = self.compositionSize//2
        i = l - (l//2)
        f = i + l
        for m in range(i,f):
            self.locus_invert(m)

    def rand_mutate(self):
        r = random.randint(0,self.compositionSize)
        for i in range(0,r):
            m = random.randint(0,self.compositionSize-1)
            self.locus_invert(m)   

    def locus_invert(self,m):
        #seleciona o locus (posição) do gene que irá sofrer mutação
        if (self.composition[m] == 1):
            self.composition[m] = 0
        else:
            self.composition[m] = 1
        
