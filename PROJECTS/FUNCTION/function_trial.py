def display (item, currency):
    
    total = sum(item.values())
    print("Expenses are :", total, currency)
    
    
values = {"Groceries": 150.0, "Transport": 50.0, "Entertainment": 100.0}
display (values, "USD")
