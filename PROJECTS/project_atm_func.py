#  This project is for GYM MEMBERSHIP while using the function


print('..........THE GYM.........')


name = input("Please Enter your name : ")
age = int(input("Please Enter your age : "))


# return name, age

    
#   def membership():
print("There are three membership availabe in GYM : ")
print("1. Basic = ₹ 1000 : ")
print("2. Premium = ₹ 2000 : ")
print("3. VIP = ₹ 3000 : ")

basic = 1000
premium = 2000
vip = 3000

choose = int(input("Please choose your Gym membership : "))

if choose == 1:
    membersip_fee = basic
    membership_name = "Basic Membership"
    memership_discount = "You Got 10% "
    # print("Basic Gym membership : ")
    # print("You've get 10% discount ")
    after_discount = basic - ((basic * 10)/100)
    membership_discount = ((basic * 10)/100)
    
elif choose == 2:
    membersip_fee = premium
    membership_name = "Premium Membership"
    memership_discount = "You Got 15% "
    # print("Premium Gym membership : ")
    # print("You've get 15% discount ")
    after_discount = premium - ((premium * 15)/100)
    membership_discount = ((premium * 15)/100)
     
    
    
elif choose == 3:
    membersip_fee = vip
    membership_name = "VIP Membership"
    memership_discount = "You Got 20% "
    # print("VIP Gym membership : ")
    # print("You've get 20% discount ")
    after_discount = vip - ((vip * 20)/100)
    membership_discount = ((vip * 20)/100)
    
else:
    print("Invalid choice ....")
    
# print(choose)

    

if age >= 18 and age <= 25:
    # special_discount =(f"Your age is {age} so you'll get additional 5% student discount")
    # print("You'll get extra 5% discount")
    total_discount = after_discount - ((after_discount*5)/100)
    student_discount = ((after_discount*5)/100)
    
    
    
elif age > 60:
    # special_discount =(f"Your age is {age} so you'll get additional 7% senior discount")
    # print("You'll get extra 7% discount")
    total_discount = after_discount - ((after_discount*7)/100)
    senior_discount = ((after_discount*7)/100)
    
else:
    total_discount = after_discount
    
    
# FINAL RECEIPT
print("..........FINAL RECEIPT..........")
print("Name : " , name)
print("Age : ", age)
print("Membership : ", membership_name)
print("Membership Discount : " , memership_discount)
print("Original Fees : ", membersip_fee)
# print("special discount : " , special_discount)

print("Membership Discount : ",membership_discount )
if age >= 18 and age <= 25:
    print(f"Your age is {age} so you'll get additional 7% student discount")
    print("Student Discount : ", student_discount)
    
elif age > 60:
    print(f"Your age is {age} so you'll get additional 7% senior discount")
    print("Senior Discount : ", senior_discount)
    

print("Total : ", total_discount)



# print('..........THE GYM.........')

# def user_data():
#     # print("Your name is : ", name)
#     # print("Your age is : ", age)
    
#     return name, age
    
# name = input("Please Enter your name : ")
# age = int(input("Please Enter your age : "))

# user_data()

# def membership_plan():
#     print("There are three membership availabe in GYM : ")
#     print("1. Basic = ₹ 1000 : ")
#     print("2. Premium = ₹ 2000 : ")
#     print("3. VIP = ₹ 3000 : ")
    
    
    
# def membership_data():
    
#     choose = int(input("Please choose your Gym membership : "))
    
#     basic = 1000
#     premium = 2000
#     vip = 3000


#     if choose == 1:
#         membersip_fee = basic
#         membership_name = "Basic Membership"
#         memership_discount = "You Got 10% "
#         # print("Basic Gym membership : ")
#         # print("You've get 10% discount ")
#         after_discount = basic - ((basic * 10)/100)
#         membership_discount = ((basic * 10)/100)
        
#     elif choose == 2:
#         membersip_fee = premium
#         membership_name = "Premium Membership"
#         memership_discount = "You Got 15% "
#         # print("Premium Gym membership : ")
#         # print("You've get 15% discount ")
#         after_discount = premium - ((premium * 15)/100)
#         membership_discount = ((premium * 15)/100)
        
        
        
#     elif choose == 3:
#         membersip_fee = vip
#         membership_name = "VIP Membership"
#         memership_discount = "You Got 20% "
#         # print("VIP Gym membership : ")
#         # print("You've get 20% discount ")
#         after_discount = vip - ((vip * 20)/100)
#         membership_discount = ((vip * 20)/100)
        
#     else:
#         print("Invalid choice ....")
    
    
    
