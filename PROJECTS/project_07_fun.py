#   My 7th project

# name = input("Enter your name : ")

# salary = int(input("Employee1 salary : "))
# bonus = int(input("Employee1 bonus : "))

# total_salary = salary + bonus


# print(f"Your name are {name} ")
# print("Your total salary is : ", total_salary)


# def salary_structure( name, salary , bonus):
    
#     print("your name : ", name)
#     print("Salary is : ", salary )
#     print("Bonus is : ", bonus)
    
#     total_salary = salary + bonus
    
#     # print("Your total salary is : ", total_salary)
    
#     return total_salary


# def employee():
#     name = input("Plz. Enter your name : ")
#     salary = int(input("Your salary is : "))
#     bonus = int(input("Your Bonus is : "))
    
#     meri_salary = salary_structure(name, salary, bonus)
    
#     print("Your Total salary is ", meri_salary)
    
#     if meri_salary >= 200:
#         print("Excellent worker")
        
#     elif meri_salary < 150:
#         print("good employee")
        
#     else :
#         print("Employee")
    
# employee()


def salary_str(name, salary, bonus):
    print("Your name : ", name)
    print("Your salar : ", salary)
    print("Your bonus : ", bonus)
    
    total_salary = salary + bonus
    
    return total_salary


def employee():
    name = input("Please enter your name : ")
    salary = int(input("Enter Your salary : "))
    bonus = int(input("enter your bonus : "))   
    
    meri_salary = salary_str(name, salary, bonus)
    
    print("My total salary is : ", meri_salary)
      
    if meri_salary > 150:
        print("Excellent man")
        
    elif meri_salary > 100:
        print("Good man")
        
    else:
        print("Empoyee")  
        
        
while True:
    employee()
    
    
    while True:
    
        choice = input("continue?  yes/no : ")
        print(choice)
        
        if choice == "yes":
            break
        
        elif choice == "no":
            break
        
        else:
            print("Invalid... Plz. give answer in YES or NO only")
        
        