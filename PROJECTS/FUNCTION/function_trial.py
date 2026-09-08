def square():
    try :
        num = int(input("Print enter the number : "))
        print("Square of number is : ", num**2)
        
    except Exception as value:
        print("Error :", value) 
        
square()
        
print("Yo")