''''add = lambda a, b : a+b
print(add(5, 3))  # Output: 8      normal lambda function 


add = lambda a, b=5 : a+b
print(add(5))  # Output: 10     lambda function with default argument


add = lambda a, b=5, c=10 : a+b+c
print(add(a =5))  # Output: 20     lambda function with default argument and keyword argument

# add = lambda a, b: a+b
# print(add(a=5, 5))  # Output: 10     lambda function with keyword argument and positional argument
# # SyntaxError: positional argument follows keyword argument


# num = lambda a,b : a+b, a-b
# print(num(5, 3))  # Output: (8, 2)     lambda function with multiple return values
# NameError: name 'a' is not defined'''


#  multiple staments in lambda function

num = lambda a,b : (a+b, a-b)
add, sub = num(20,10)
print(add)  # Output: 30
print(sub)  # Output: 10