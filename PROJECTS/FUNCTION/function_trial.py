def items(name, employee1 = "yoyo"):
    employee1 = employee1 + " " + name
    print("update value is :", employee1, name)
    
items("John")
print(items.__defaults__ )
items("John", "lucifer")
items("John")
items("John")

