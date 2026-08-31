def items(name, employee_data = None):
    if employee_data is None:
        employee_data = []
    employee_data.append(name)
    print("update value is :", employee_data, name)
        
items("John")
print(items.__defaults__)
employee_data = items("Jane")
print(items.__defaults__)
items("Doe", ["Alice", "Bob"])
print(items.__defaults__)
