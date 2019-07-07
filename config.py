#define o tamanho de cada gene cromossomo (indivíduo)
#que também representa o número de elementos disponíveis para adicionar na mochila
composition_size = 10

dataset = "example1"

#número de cromossomos (indivíduos) que deve existir em cada população gerada
population_size = 15

#número de gerações (rodadas)
generations = 24

#define o método para mutação de genes: "random", "fix" ou "none"
mutateMethod = "random" 

#define o método de procriação (geração de nova população): "first_elite", "all_elite" ou "random"
procreateMethod = "first_elite"