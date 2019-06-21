import random

available_itens_weight = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
available_itens_value  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

class Cromossomo:

    def __init__(self):

        self.weight = 0
        self.value = 0
        self.compositionSize = 10
        self.composition = [0 for i in range(self.compositionSize)]
        self.fit = False
    
    def initialize(self):
        # define 0s e 1s aleatorios para compor o cromossomo
        for i in range(self.compositionSize):
            self.composition[i] = random.randint(0,1)
        self.calc()
    
    def calc(self):
        self.value = 0
        self.weight = 0
        for i in range(self.compositionSize-1):
            if (self.composition[i] == 1):
                self.value += available_itens_value[i]
                self.weight += available_itens_weight[i]

    def evaluate_fitness(self, expected_weight):

        if (self.weight <= expected_weight):
            self.fit = True
        else:
            self.fit = False
        
