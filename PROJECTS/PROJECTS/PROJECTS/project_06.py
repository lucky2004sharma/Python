import random


# def check_guess(user_guess, secret_number):
#     if user_guess < secret_number:
#         print("Too low! Try again.")
#         return False
#     elif user_guess > secret_number:
#         print("Too high! Try again.")
#         return False
#     else:
#         print(f"🎉 Correct! The number was indeed {secret_number}!")
#         return True


# def play_game():
#     print("Welcome to the Number Guessing Game!")
#     print("I am thinking of a number between 1 and 20.")

#     target_number = random.randint(1, 20)
#     attempts = 0
#     game_won = False

#     while not game_won:
#         guess = int(input("Enter your guess: "))
#         attempts = attempts + 1

#         game_won = check_guess(guess, target_number)

#     print(f"You won the game in {attempts} attempts!")


# # This starts the game
# play_game() 



print("This is a random no. guess")

computer_num = random.randint(1,10)
atempt = 0

while True:
    guess = int(input("Enter youur number : "))
    
    if guess > computer_num:
        print("Your guess is big : ")
        atempt = atempt + 1
        
    elif guess == computer_num:
         print("You guessed correct number : ")
         atempt = atempt + 1
         print(f"you guess in {atempt} atempts ")
         break
        
    else:
        print("the number is low")
        atempt = atempt +1
        
        
    
        
        
    
