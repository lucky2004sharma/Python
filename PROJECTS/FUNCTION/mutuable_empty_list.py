data = [5,10,15,20,25,30]

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
# print(list(filtered_data())) # []  # filter object is exhausted after first iteration, so it returns empty list  