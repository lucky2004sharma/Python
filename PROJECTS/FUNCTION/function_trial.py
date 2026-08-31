# def items(name, employee= []):
#     employee.append(name)
#     print("update value is :", employee)
#     # return employee


# add_employee = items("John")
# print(items.__defaults__)
# add_employee = items("Jane")
# print(items.__defaults__)
# add_employee = items("Doe")
# print(items.__defaults__)

def items(name, employee1=None):
    if employee1 is None:
        employee1 = []
        # employee1 = [name]

    employee1.append(name)
    print("update value is :", employee1)
    
items("John")
print(items.__defaults__)

add_employee = items("Jane")
print(items.__defaults__)           

add_employee = items("Doe", ["Alice", "Bob"])
print(items.__defaults__)