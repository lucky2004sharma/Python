name = ['om', 'jay','shiv','rahul','sachin']
def check_len(name):
    return len(name)

lengths = map(check_len, name)
print(lengths)
print(type(lengths))
print(list(lengths))