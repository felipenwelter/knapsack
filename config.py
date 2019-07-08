dataset = "example2"

#número de cromossomos (indivíduos) que deve existir em cada população gerada
population_size = 15

#número de gerações (rodadas)
generations = 24

#define o método para mutação de genes: "random", "fix" ou "none"
mutateMethod = "random" 

#define o método de procriação (geração de nova população): "first_elite", "all_elite" ou "random"
procreateMethod = "all_elite"


'''
example2 - 15 itens
    brute force spent 6.118438959121704 sec to find 749 kg to 1458 of value
    brute force spent 14.897922039031982 sec to find 749 kg to 1458 of value
    brute force spent 10.612521171569824 sec to find 749 kg to 1458 of value
    genetic algorithm spent 0.3794059753417969 sec to find 736 kg to 1406 of value
    genetic algorithm spent 0.02741694450378418 sec to find 738 kg to 1425 of value 
    genetic algorithm spent 0.48957204818725586 sec to find 749 kg to 1441 of value

example3 - 20 itens
    brute force spent 238.15140390396118 sec to find 4362713 kg to 12585215 of valuee
    genetic algorithm spent 0.44092679023742676 sec to find 4204943 kg to 9722923 of value

example4 - 24 itens
    brute force spent 3427.5045800209045 sec to find 6402560 kg to 13549094 of value
    brute force spent 3990.657341003418 sec to find 6402560 kg to 13549094 of value
    genetic algorithm spent 0.02862381935119629 sec to find 5971823 kg to 12272762 of value
    genetic algorithm spent 0.8132588863372803 sec to find 6300348 kg to 12730922 of value

example5 - 30 itens
    genetic algorithm spent 0.8425750732421875 sec to find 8920054 kg to 29790475 of value

example6 - 60 itens
    genetic algorithm spent 1.0823321342468262 sec to find 768981962 kg to 9058338950 of value

example7 - 80 itens
    genetic algorithm spent 0.8267860412597656 sec to find 1033636605 kg to 14198770650 of value
    genetic algorithm spent 0.32483792304992676 sec to find 1074772832 kg to 11276460470 of value

example8 - 120 itens
    genetic algorithm spent 1.8189539909362793 sec to find 1505780656 kg to 16731436533 of value
    genetic algorithm spent 1.4101293087005615 sec to find 1519209617 kg to 17357478658 of value

example9 - 240 itens
    genetic algorithm spent 2.3269708156585693 sec to find 3259655372 kg to 32923331824 of value
    genetic algorithm spent 2.749253273010254 sec to find 3206261257 kg to 34907161088 of value

example10 - 480 itens
    genetic algorithm spent 3.791088104248047 sec to find 6585061213 kg to 67775445591 of value
    genetic algorithm spent 3.276181936264038 sec to find 6590583864 kg to 68987213673 of value
'''