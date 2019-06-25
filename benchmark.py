from bruteforce import bruteForce
from main import geneticAlgorithm
import time as t

start = t.time()
resp1 = bruteForce()
time1 = t.time() - start

start = t.time()
resp2 = geneticAlgorithm()
time2 = t.time() - start

print(f" brute force spent {time1} sec to find {resp1.weight} kg to {resp1.value} of value")
print(f" genetic algorithgm spent {time2} sec to find {resp2.weight} kg to {resp2.value} of value")