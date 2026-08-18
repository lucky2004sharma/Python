def factorial(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    result = 1

    for value in range(2, number + 1):
        result *= value

    return result


def fibonacci(count):
    if count < 0:
        raise ValueError("Count cannot be negative.")

    sequence = []
    first, second = 0, 1

    for _ in range(count):
        sequence.append(first)
        first, second = second, first + second

    return sequence


def main():
    print("Factorial and Fibonacci Program")
    print("1. Calculate factorial")
    print("2. Generate Fibonacci sequence")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            number = int(input("Enter a non-negative number: "))
            print(f"Factorial of {number}: {factorial(number)}")

        elif choice == "2":
            count = int(input("How many Fibonacci numbers? "))
            print("Fibonacci sequence:", fibonacci(count))

        else:
            print("Invalid choice.")

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()