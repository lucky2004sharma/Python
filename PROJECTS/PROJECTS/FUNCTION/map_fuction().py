'''name = ['om', 'jay','shiv','rahul','sachin']
def check_len(name):
    # return len(name) # only print the length of each name in the list
    # return name # only print the name in the list
    return name, len(name) # print the name and length of each name in the list

lengths = map(check_len, name)
print(lengths)
print(type(lengths))
# print(list(lengths))
for element in lengths:
    # print(type(element))
    # print(element) # print the name and length of each name in the list
    print(element[0], element[1]) # print the name and length of each name in the list
    
    
# print square of each number in the list

numbers = [1, 2, 3, 4, 5]
def square(num):
    return num ** 2

squared_numbers = map(square, numbers)
# print(list(squared_numbers)) # print the square of each number in the list
for element in squared_numbers:
    print(element)
    
    
# by lambda function

numbers = [ 2, 3, 4, 5, 6]

squared_number = map( lambda num : num ** 2, numbers)
print(list(squared_number))'''



numbers = [1, 2, 3, 4, 5]
def square(num):
    if num % 2 != 0:
        return num ** 2
    else:
        return num

squared_numbers = map(square, numbers)
print(list(squared_numbers)) # print the square of each number in the list
# for element in squared_numbers:
#     print(element)