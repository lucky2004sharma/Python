def display(item, currency):
    total = sum(item.values())
    print("\nExpenses:", total)
    

cart = {"Groceries": 150.0, "Transport": 50.0, "Entertainment": 100.0}
display(cart, "₹")