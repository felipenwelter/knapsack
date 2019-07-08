import random
import json

'''
Rotina com o objetivo de criar arquivos de dataset de teste
será necessário apenas modificar as variáveis fileName e capacity
'''

fileName = "example10"
capacity = 480
values = []
weights = []

for x in range(capacity):
  weights.append(random.randint(50 * 100000, 500 * 100000))

for x in range(capacity):
  values.append(random.randint(500 * 100000, 5000 * 100000))

data = {
    "capacity": sum(weights) / 2,
    "values": values,
    "weights": weights
}
with open(f"datasets/{fileName}.json", "w") as outfile:
    json.dump(data, outfile)