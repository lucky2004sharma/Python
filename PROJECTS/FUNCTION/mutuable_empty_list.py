'''data = [5,10,15,20,25,30]

def even_num(data):
    if data % 2 == 0:
        return True
    else:
        return False
    
filtered_data = filter(even_num, data)

print(filtered_data) # 0<filter object at 0x0000020D9A1B7C10>
print(type(filtered_data)) # <class 'filter'>
# for element in filtered_data:
#     print(element) # 10, 20, 30

print(list(filtered_data)) # []  # filter object is exhausted after first iteration, so it returns empty list
# print(list(filtered_data())) # []  # filter object is exhausted after first iteration, so it returns empty list  '''

# data = [5,10,15,20,25,30]
# def even_num(data):
#     return data % 2 == 0  # it's return True or False based on the condition, so we don't need to use if-else statement not need to use return True or return False, it will automatically return True or False based on the condition

# filtered_data = filter(even_num, data)
# print(list(filtered_data)) # [10, 20, 30]  

# by using lambda function


data = [5,10,15,20,25,30]

filtered_data = filter( lambda num : num % 2 ==0, data)
print(list(filtered_data))
