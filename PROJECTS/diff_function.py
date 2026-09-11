expenses = []

while True:
    amount = input("Enter expense (or done): ")

    if amount == "done":
        break

    expenses.append(int(amount))

print("Today's expenses:")

for amount in expenses:
    print("₹", amount)

print("Total:", sum(expenses))