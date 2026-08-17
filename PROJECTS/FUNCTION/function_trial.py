import random

def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        user_guess = input("Enter your guess (or 'q' to quit): ")
        if user_guess.lower() == 'q':
            print(f"The number was {number_to_guess}. Goodbye!")
            break
            
        try:
            guess = int(user_guess)
            attempts += 1
            
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    play_game()