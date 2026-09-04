'''import functools

data = [1,2,3,4,5]


def addition(a, b):
    a = a + b
    return a 

full_sum = functools.reduce(addition, data)
print(full_sum) # print the sum of all numbers in the list

# by lambda function

import functools

data = [ 1,2,3,4,5 ]

full_sum = functools.reduce(lambda a, b : a+b, data)
print(full_sum)'''

from functools import partial

# data = [1,2,55,4,5]

# def max(a, b):
#     if a > b:
#         return a
#     else:
# 	    return b

# max_number = functools.reduce(max, data)
# print(max_number)

def addition(a,b,c,d):
    return a + b + c + d

value = partial(addition, a =5, b =10)
print(value(c=15, d=20)) # output = 50