num = int(input("Enter a number: "))
steps = [num]
while num >= 10:
    num = sum(int(d) for d in str(num))
    steps.append(num)
print(" -> ".join(map(str, steps)))
print("Digital root:", steps[-1])