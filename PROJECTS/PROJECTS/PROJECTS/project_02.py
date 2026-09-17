import random

number = random.randint(0,10)

print("This is my second project")

guess = 0

while guess!= number:
    guess = int(input("Enter the number :"))

    if guess == number:
        print("The number is correct")

        
    elif guess > number:
        print("This is high number")

    else:
        print("This is low number") 