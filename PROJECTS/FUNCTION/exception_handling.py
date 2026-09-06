try :
    
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError
    print("your age is ", age)
    
except ValueError :
    print("Enter valid age ")
    