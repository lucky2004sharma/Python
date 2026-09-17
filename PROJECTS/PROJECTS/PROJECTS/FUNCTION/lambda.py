# # '''# WHY USE THE LAMBDA FUNCTION?

# # # print(sorted([5,7,65,89,66,4,22,55]))

# # data = ['tendulkar sachin', 'kohli virat', 'dravid rahul', 'dhoni ms', 'sehwag virender']

# # sorted_data = sorted(data)
# # print(sorted_data) # sorted in alphabetical order


# # sorted_data = sorted(data, key=len)
# # print(sorted_data) # sorted in ascending order of length of string

# # # split funciton
# # print('sharma rohit'.split( )) # output = ['sharma', 'rohit']  # split the string into list of words
# # print('sharma rohit'.split()[1])  # ['sharma'=0, 'rohit'=1]  # output = rohit'''


# # # def sort_by_last_name(name1):
# # #     first_name = name1.split()[1]
# # #     return first_name
    
# # # data = ['tendulkar sachin', 'kohli virat', 'dravid rahul', 'dhoni ms', 'sehwag virender']
# # # print(sorted(data, key=sort_by_last_name)) # sorted in ascending order of last name

# # # by lambda function

# # # data = ['tendulkar sachin', 'kohli virat', 'dravid rahul', 'dhoni ms', 'sehwag virender']
# # # print(sorted(data, key = lambda name : name.split()[1])) # sorted in ascending order of last name

# # def change_name(name1):
# #     first_name = name1.split()[1]
# #     return first_name

# # data = ['tendulkar sachin', 'kohli virat', 'dravid rahul', 'dhoni ms', 'sehwag virender']
# # print(sorted(data, key = change_name)) # sorted in ascending order of last name





# def outer(): # by normal function
#     def add(a, b):
#         return a + b
#     return add


# additon = outer()
# print(additon(5, 6)) 

# def outer(): # by lambda function
#     add = lambda a, b : a + b
#     return add

# addition = outer()
# print(addition(5, 6))

# # nested lambda function

# outer = lambda : (lambda a, b : a + b)
# addition = outer()  
# print(addition(5, 10))

# outer =  lambda a, b : a + b

# print(outer(5, 10))


#  Lambda function with if-else statement

num1 = 10 # normal if-else statemnt
num2 = 20

if num1>num2:
    print("num1 is greater than num2", num1 )
else:
    print("num2 is greater than num1", num2 )
    
# short hand if-else statemnt

print(10 if num1>num2 else 20) # output = 20

# lambda function with if-else statement

num1 = 110
num2 = 220

max = lambda num1, num2: num1 if num1>num2 else num2
print(max(num1, num2)) # output = 220