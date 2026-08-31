def items(name, employee= []):
    employee.append(name)
    print("update value is :", employee)
    # return employee


add_employee = items("John")
print(items.__defaults__)
add_employee = items("Jane")
print(items.__defaults__)
add_employee = items("Doe")
print(items.__defaults__)