import functools

data = [1,2,3,4,5,6,7,8,9,10]


def addition(a, b):
    a = a + b
    return a + b

full_sum = functools.reduce(addition, data)
print(full_sum) # print the sum of all numbers in the list