# exception example number should not be divisible by 5

class FiveDivisionError(Exception):
    
    pass

n1 = int(input("Enter the 1st number "))
n2 = int(input("Enter the 2nd number "))
try:
    if n2 == 5:
        raise FiveDivisionError("Doesn't by 5")
    div = n1/n2
    print("Division is ", div)
    
except (FiveDivisionError, ZeroDivisionError) as var :
    print("error :", var)
    
print("Stop")

    
    