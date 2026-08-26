class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("₹", amount, "deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("₹", amount, "withdrawn successfully.")
        else:
            print("Insufficient balance!")

    def show_balance(self):
        print("Account Holder:", self.name)
        print("Current Balance: ₹", self.balance)


# Create account
account1 = BankAccount("Mohit", 5000)

account1.show_balance()

account1.deposit(2000)

account1.withdraw(1500)

account1.show_balance()