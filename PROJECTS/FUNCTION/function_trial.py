def items(name, employee= []):
    employee.append(name)
    print(employee)
    return employee


add_employee = items("John")
add_employee = items("Jane")
add_employee = items("Doe", add_employee)