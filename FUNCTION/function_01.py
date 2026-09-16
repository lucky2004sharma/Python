expenses = []

while True:
    print("\n1. Add expense")
    print("2. Show expenses")
    print("3. Show total")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Expense name: ")
        amount = float(input("Amount: ₹"))
        expenses.append((name, amount))
        print("Expense added.")

    elif choice == "2":
        if not expenses:
            print("No expenses recorded.")
        else:
            for name, amount in expenses:
                print(f"{name}: ₹{amount:.2f}")

    elif choice == "3":
        total = sum(amount for _, amount in expenses)
        print(f"Total: ₹{total:.2f}")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")