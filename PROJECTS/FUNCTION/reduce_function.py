'''import functools

data = [1,2,3,4,5]


def addition(a, b):
    a = a + b
    return a 

full_sum = functools.reduce(addition, data)
print(full_sum) # print the sum of all numbers in the list'''

# by lambda function

import functools

data = [ 1,2,3,4,5 ]

full_sum = functools.reduce(lambda a, b : a+b, data)
print(full_sum)