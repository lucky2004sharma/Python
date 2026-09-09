class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def show_balance(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


account1 = BankAccount("Mohit", 5000)

account1.show_balance()