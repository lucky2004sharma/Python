# exception example number should not be divisible by 5

class FiveDivisionError(Exception):
    # this is exception class called when number is try to divide by 5
    # def __init__(self):
    #     print("cannot divide by 5")  # just for information
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

    
    