print("this is student result")

subject1 = int(input("enter no. of subject 1st:"))
subject2 = int(input("enter no. of subject 2nd:"))
subject3 = int(input("enter no. of subject 3rd:"))

sum = subject1 + subject2 + subject3 
percent = sum/3

if (percent >= 40):
    print("student is pass" , percent)

else:
    print("student is fail", percent)

if ( subject1<= 33 or subject2 <=33 or subject3<= 33):
    print("student is also fail")

else:
    print("student is pass")

print("end of result")