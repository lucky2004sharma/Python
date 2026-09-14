import random

rolls = int(input("How many times to roll a die? "))
results = [random.randint(1, 6) for _ in range(rolls)]
print("Rolls:", results)
print("Average:", sum(results) / rolls)
print("Most common:", max(set(results), key=results.count))