def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def main():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Choose an operation (1-4): ")

    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))

        operations = {
            "1": ("Result", add),
            "2": ("Result", subtract),
            "3": ("Result", multiply),
            "4": ("Result", divide),
        }

        if choice not in operations:
            print("Invalid operation.")
            return

        label, operation = operations[choice]
        print(f"{label}: {operation(first_number, second_number)}")

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()