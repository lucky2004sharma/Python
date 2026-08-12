# print("THIS IS MAIN DIFFERENCE BETWEEN FUNCTION ")

# #   this is to print result of three students without function

# name = input('Enter your name : ')

# print("There are five subject")


# print(f"The first student name is {name} ")

# math = int(input("math : "))
# physics = int(input("physics : "))
# chemistry = int(input("chemistry : "))
# english = int(input("english : "))
# hindi = int(input("hindi : "))

# total = math + physics + chemistry + english + hindi
# percent = (total * 100)/ 500
# total = print("the total sum of marks are", total)
# percent = print("total percentage are : ", percent)


# name = input('Enter your name : ')
# print(f"The first student name is {name} ")

# math = int(input("math : "))
# physics = int(input("physics : "))
# chemistry = int(input("chemistry : "))
# english = int(input("english : "))
# hindi = int(input("hindi : "))

# total = math + physics + chemistry + english + hindi
# percent = (total * 100)/ 500
# total = print("the total sum of marks are", total)
# percent = print("total percentage are : ", percent)



# name = input('Enter your name : ')
# print(f"The first student name is {name} ")


# math = int(input("math : "))
# physics = int(input("physics : "))
# chemistry = int(input("chemistry : "))
# english = int(input("english : "))
# hindi = int(input("hindi : "))

# total = math + physics + chemistry + english + hindi
# percent = (total * 100)/ 500
# total = print("the total sum of marks are", total)
# percent = print("total percentage are : ", percent)



#  NOW CODE WITH FUNCTION AND HOW TO DO THIS IN LESS LINE


# def stu_result(name, math, physics, chemistry, hindi):
#     print(" your name : ", name)
#     print("Your physics marks are : ", physics)
#     print("Your math marks are : ", math)
#     print("Your chemistry marks are : ", chemistry)
#     print("Your hindi marks are : ", hindi)
    
#     total = math + physics + chemistry + hindi
#     Percent = (total * 100) / 400
#     print("total ", total)
#     print("percentage " , Percent)
    


# name = input("Enter your name : ")
# physics = int(input("physics : "))
# math = int(input("math : "))
# chemistry = int(input("chemistry : "))
# hindi = int(input("hindi : "))
# stu_result( name, math, physics,  chemistry, hindi)


# name = input("Enter your name : ")
# physics = int(input("physics : "))
# math = int(input("math : "))
# chemistry = int(input("chemistry : "))
# hindi = int(input("hindi : "))
# student2 = stu_result( name, physics, math, chemistry, hindi)



# name = input("Enter your name : ")
# physics = int(input("physics : "))
# math = int(input("math : "))
# chemistry = int(input("chemistry : "))
# hindi = int(input("hindi : "))
# student3 = stu_result( name, physics, math, chemistry, hindi)



#  ANOTHER FULLY FUNCTION CODE

def stu_result(name, math, physics, chemist, hindi):
    
    print("\n------ RESULT ------")
    print("Your name ", name)
    print("math : ", math)
    print("Physics : ", physics)
    print("chemist : ", chemist)
    print("hindi : ", hindi)
    
    total = math + physics + chemist + hindi
    percent = (total * 100) / 400
    
    print("Total marks : ", total)
    print("Percentage are : ", percent)
    
    
def student_data():
    name = input("enter your name : ")
    print(f"The student name is {name}")
    math = int(input(" Maths marks are : "))
    physics = int(input(" physics marks are : "))
    chemist = int(input(" chemist marks are : "))
    hindi = int(input(" Hindi marks are : "))
    
    stu_result(name, math, physics, chemist, hindi)
    
student_data()
student_data()
student_data()  