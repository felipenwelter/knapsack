import config
import json
from cromossomo import Cromossomo


def composition_size() -> int:
    with open(f'datasets/{config.dataset}.json') as json_file:
        data = json.load(json_file)
    return len(data["values"])


def bruteForce():
    compositionSize = composition_size()
    limit = pow(2, compositionSize) - 1
    best = Cromossomo()

    for i in range(limit):

        print(f"Brute Force limit {i}", end='\r')

        new_composition = list(bin(i)[2:].zfill(compositionSize))
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

    print("\nKnapsack Problem - Brute Force")
    print("A melhor resposta encontrada foi:")
    print(f"composition: {best.composition}")
    print(f"value: {best.value}")
    print(f"weight: {best.weight}")

    return best
