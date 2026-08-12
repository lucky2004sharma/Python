print("Hello! This is my first project")

name = input("Enter the student name: ")

print("There are five subjects")

subject1 = int(input("Enter the 1st subject marks :"))
subject2 = int(input("Enter the 2nd subject marks :"))
subject3 = int(input("Enter the 3rd subject marks :"))
subject4 = int(input("Enter the 4th subject marks :"))
subject5 = int(input("Enter the 5th subject marks :"))

marks = subject1 + subject2 + subject3 + subject4 + subject5
percent = (marks * 100) / 500



if percent > 90:
    Grade = "A+"

elif percent >= 80:
    Grade = "A"

elif percent >= 70:
    Grade = "B"

elif percent >= 60:
    Grade = "C"

elif percent >= 40:
    Grade = "D"

else:
    Grade = "Fail"


if percent >= 40:
    Result = "pass"

else:
    Result = "Fail"


print("THE RESULT ARE")

print("Name :", name)
print("Total marks :", marks)
print("Total percentage :",percent)
print("Grad :", Grade)
print("Result :", Result)


