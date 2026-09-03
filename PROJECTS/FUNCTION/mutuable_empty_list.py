def get_name():
    first_name = input("Enter your first name : ")
    last_name = input("Enter your last name : ")
    return first_name + " " + last_name

get_name = get_name()
print(get_name)


def get_name(first_name, last_name):
    return first_name + " " + last_name
    
    

first_name = input("Enter your first name : ")
last_name = input("Enter your last name : ")
print(get_name(first_name, last_name))
