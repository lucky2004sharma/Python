# ATM MACHINE WITH TRY AND EXCEPTION.

def password():
    user_pin = 1234
    pin = int(input("Please enter the pin : ", pin))
    if user_pin == pin:
        return 'welcome '
    else:
        return 'Wrong PIN : '
    
def withdraw(balance,user_withdraw):
    # print("How much money you want to withdraw : ")
    if user_withdraw>=10000:
        return "insuficient fund"
    elif user_withdraw>=9000:
        return 'At least one thousanbd should be in account'
    else:
        after_withdraw = balance - user_withdraw
        return after_withdraw
    
def deposit(balance,user_deposit):
    print("How much money you want to deposit : ")
    after_deposit = balance + user_deposit
    return after_deposit


print("----------- WELCOME TO ATM ----------")


while True:
    print("1. Check balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    balance = 10000
    
    choice = int(input("Choose what you want to search : "))
    if choice == 1:
        print("Thank you for checking the balance : ", balance)
        
    elif choice ==2:
        user_withdraw = int(input("How much money you want to withdraw Please enter the amount : "))
        withdraw_amount = withdraw(balance,user_withdraw)
        print("Message : ", withdraw_amount)
        
    elif choice == 3:
        user_deposit = int(input("Enter the amount to deposit : "))

        deposit_amount= deposit(balance,user_deposit)
        print("Money after deposit : ", deposit_amount)
        
        
    else:
        print("choose between 1, 2 and 3")
        break
        
