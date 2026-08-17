import random
import string

def generate_secure_password(length):
    if length < 4:
        return "Error: Password must be at least 4 characters long."
        
    all_chars = string.ascii_letters + string.digits + string.punctuation
    # Ensure at least one of each type is included
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    # Fill the rest randomly
    password += [random.choice(all_chars) for _ in range(length - 4)]
    random.shuffle(password)
    return "".join(password)

if __name__ == "__main__":
    print("--- Secure Password Generator ---")
    try:
        user_length = int(input("Enter desired password length: "))
        print(f"Your new password is: {generate_secure_password(user_length)}")
    except ValueError:
        print("Please enter a valid whole number.")