import random

available_itens_weight = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
available_itens_value  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

class Cromossomo:

    def __init__(self):

        self.weight = 0
        self.value = 0
        self.composition = [0 for i in range(10)]
    
    def initialize(self):
        for i in range(len(self.composition)):
            self.composition[i] = random.randint(0,1)
            if (self.composition[i] == 1):
                self.value += available_itens_value[i]
                self.weight += available_itens_weight[i]