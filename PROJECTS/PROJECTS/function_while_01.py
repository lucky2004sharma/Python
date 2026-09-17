# def apply_discount(price, discount):
#     total_discount = price * (discount/100)
#     final_price = price - total_discount
#     return final_price

# shirt = apply_discount(100,10)
# print(shirt)    


# 2.

# def greet(user):
#     print(f"Hello {user}")
    
# while True:
    
#     name = input("please enter your name : ")
    
#     if name == "exit":
#         print('Programm end here')
#         break
    
#     greet(name)
    
    
def addition(x,y):
    
    sum = x+y
    
    # value =  print("The addition of these quesitons are : ", sum )
    return sum

while True:
    
    num1 = int(input("Enter the 1st no. : "))
    num2 = int(input("enter the 2nd no. : "))
    
    addition(num1 , num2)
    
    choie = input("continue? (yes/no)")
    if choie == "no":
        break