# def display (item, currency):
    
#     total = sum(item.values())
#     print("Expenses are :", total, currency)
    
    
# values = {"Groceries": 150.0, "Transport": 50.0, "Entertainment": 100.0}
# display (values, "USD")


def display(item, currency):
    total = sum(item.values())
    if total > 100:
        print("Expenses are:", total, currency)
        
    elif total >200:
        print("Expenses are:", total, currency)
    
    else:
        print("Expenses are:", total, currency)
    
    
car = {"Fuel": 100.0, "Maintenance": 50.0, "Insurance": 200.0}
display(car, "USD")

