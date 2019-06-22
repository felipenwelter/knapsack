#define o tamanho de cada gene cromossomo (indivíduo)
#que também representa o número de elementos disponíveis para adicionar na mochila
composition_size = 10

#peso dos itens da mochila (respectivo ao valor)
available_itens_weight = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
#valor dos itens da mochila (respectivo ao peso)
available_itens_value  = [3, 2, 1, 9,  4,  3,  5,  3,  1,  2]

#capacidade máxima de peso para a mochila, em kg
knapsackCapacity = 30

#número de cromossomos (indivíduos) que deve existir em cada população gerada
population_size = 15

#número de gerações (rodadas)
generations = 24

#define o método para mutação de genes: "random", "fix" ou "none"
mutateMethod = "random" 

#define o método de procriação (geração de nova população): "first_elite", "all_elite" ou "random"
procreateMethod = "first_elite"