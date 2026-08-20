def process_sales_data(sales):
    """
    sales: list of dicts like {"name": "Alice", "amount": 1200}
    Returns a summary dictionary.
    """
    total = sum(record["amount"] for record in sales)
    average = total / len(sales) if sales else 0
    top_performer = max(sales, key=lambda r: r["amount"]) if sales else None
 
    return {
        "total_sales": total,
        "average_sale": round(average, 2),
        "top_performer": top_performer["name"] if top_performer else None,
        "top_amount": top_performer["amount"] if top_performer else None,
    }
 
 
if __name__ == "__main__":
    sales_records = [
        {"name": "Alice", "amount": 1200},
        {"name": "Bob", "amount": 950},
        {"name": "Charlie", "amount": 1730},
        {"name": "Diana", "amount": 800},
    ]
 
    summary = process_sales_data(sales_records)
    for key, value in summary.items():
        print(f"{key}: {value}")