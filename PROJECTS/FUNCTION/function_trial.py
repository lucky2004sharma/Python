n = int(input("Enter a starting number: "))
steps = 0
while n != 1:
    print(n, end=" -> ")
    n = n // 2 if n % 2 == 0 else 3 * n + 1
    steps += 1
print(f"1 (reached in {steps} steps)")