def sum (a, b, c):
    sum = a + b + c
    return sum  

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

value = sum(a, b, c)
print("The sum of these three number is : ", value)