import sys

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

try :
    div = num1/num
    print("divison is ", div)
    
except: 
    print(sys.exc_info()[0])