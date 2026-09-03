name = ['om', 'jay','shiv','rahul','sachin']
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
    

    
    