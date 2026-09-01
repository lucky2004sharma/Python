'''# WHY USE THE LAMBDA FUNCTION?

# print(sorted([5,7,65,89,66,4,22,55]))

data = ['tendulkar sachin', 'kohli virat', 'dravid rahul', 'dhoni ms', 'sehwag virender']

sorted_data = sorted(data)
print(sorted_data) # sorted in alphabetical order


sorted_data = sorted(data, key=len)
print(sorted_data) # sorted in ascending order of length of string

# split funciton
print('sharma rohit'.split( )) # output = ['sharma', 'rohit']  # split the string into list of words
print('sharma rohit'.split()[1])  # ['sharma'=0, 'rohit'=1]  # output = rohit'''


# def sort_by_last_name(name1):
#     first_name = name1.split()[1]
#     return first_name
    
# data = ['tendulkar sachin', 'kohli virat', 'dravid rahul', 'dhoni ms', 'sehwag virender']
# print(sorted(data, key=sort_by_last_name)) # sorted in ascending order of last name

# by lambda function

# data = ['tendulkar sachin', 'kohli virat', 'dravid rahul', 'dhoni ms', 'sehwag virender']
# print(sorted(data, key = lambda name : name.split()[1])) # sorted in ascending order of last name

def change_name(name1):
    first_name = name1.split()[1]
    return first_name

data = ['tendulkar sachin', 'kohli virat', 'dravid rahul', 'dhoni ms', 'sehwag virender']
print(sorted(data, key = change_name)) # sorted in ascending order of last name
