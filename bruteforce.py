import config
from cromossomo import Cromossomo


def bruteForce():

    limit = pow(2, config.composition_size) - 1
    best = Cromossomo()

    for i in range(limit):

        new_composition = list(bin(i)[2:].zfill(config.composition_size))
        new_composition = map(lambda x: int(x), new_composition)
        new_composition = list(new_composition)

        c = Cromossomo()
        c.composition = new_composition
        c.evaluate_fitness()

        if (c.fitness):
            if (c.value > best.value):
                best = c
            elif (c.value == best.value) and (c.weight <= best.weight):
                best = c

    print("Knapsack Problem - Brute Force")
    print("A melhor resposta encontrada foi:")
    print(f"composition: {best.composition}")
    print(f"value: {best.value}")
    print(f"weight: {best.weight}")

    return best
