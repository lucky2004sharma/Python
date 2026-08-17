def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error: Division by zero"

def calculator():
    print("--- Simple Python Calculator ---")
    print("Select operation: 1.Add  2.Subtract  3.Multiply  4.Divide")

    while True:
        choice = input("Enter choice (1/2/3/4) or 'q' to quit: ")
        if choice.lower() == 'q':
            print("Exiting calculator...")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            if choice == '1': print(f"Result: {add(num1, num2)}")
            elif choice == '2': print(f"Result: {subtract(num1, num2)}")
            elif choice == '3': print(f"Result: {multiply(num1, num2)}")
            elif choice == '4': print(f"Result: {divide(num1, num2)}")
        else:
            print("Invalid Input")

if __name__ == "__main__":
    calculator()