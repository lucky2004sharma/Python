print("This is my 4th project")


name = input("Please Enter your name :")
print(f"Welcome to {name} ATM")    

PIN = 1234

atempts = 4
while atempts > 0:
    user_pin = int(input("Plz. Enter your PIN :"))

    if user_pin == PIN:
        print("You enter Correct PIN :")
        print("Welcome to ATM :\n")
        break


    else:
        print("Wrong PIN :")
        atempts = atempts -1
        print(f"You got {atempts} more atempts")
        
else:
    print('You attempts more than 3 times so your Account is blocked')

balance = 1000

while True:
    
    print("1. Check Balance :")
    print("2. Deposit Money :")
    print("3. Withdraw Money :")
    print("4. Exit\n")


    choose = int(input("Choose options :"))


    if choose == 1:
        print("Your available balance is :\n",balance)
        
    elif choose == 2:
        amount = int(input("Enter Amount :"))
        deposit_money = balance + amount
        balance = deposit_money
        print("New Balance :\n", balance)
        
    elif choose == 3:
        amount = int(input("Entter Amount :"))
        
        
        
        if amount > balance:
            print("Insufficient amount")
            
        else:
            withdraw_money = balance - amount
            balance = withdraw_money
            print("New Balance :\n", withdraw_money)
            
        
    elif choose == 4:
        print("Transaction End\n")
        break
    
    
    else:
        print("Invalid Option :\n")
        
    