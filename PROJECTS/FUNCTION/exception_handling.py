def divide(num1, num2):
    
    try:
        divi = num1/num2
        return divi
        
    except ZeroDivisionError as obj:
        print("Error : ", obj)
        

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

divided_value = divide(num1, num2)
print("The division of", num1, "and", num2, "is:", divided_value)