class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []
 
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive")
            return
        self.balance += amount
        self.history.append(f"Deposited {amount}")
        print(f"{self.owner} deposited {amount}. New balance: {self.balance}")
 
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds for {self.owner}")
            return
        self.balance -= amount
        self.history.append(f"Withdrew {amount}")
        print(f"{self.owner} withdrew {amount}. New balance: {self.balance}")
 
    def transfer(self, other_account, amount):
        if amount > self.balance:
            print("Transfer failed: insufficient funds")
            return
        self.withdraw(amount)
        other_account.deposit(amount)
        print(f"Transferred {amount} from {self.owner} to {other_account.owner}")
 
 
if __name__ == "__main__":
    alice = BankAccount("Alice", 1000)
    bob = BankAccount("Bob", 500)
 
    alice.deposit(200)
    bob.withdraw(100)
    alice.transfer(bob, 300)
 
    print(f"\nFinal balances -> Alice: {alice.balance}, Bob: {bob.balance}")