class Inventory:
    def __init__(self, low_stock_threshold=5):
        self.items = {}
        self.low_stock_threshold = low_stock_threshold
 
    def add_stock(self, item_name, quantity):
        self.items[item_name] = self.items.get(item_name, 0) + quantity
        print(f"Added {quantity} of '{item_name}'. Total: {self.items[item_name]}")
 
    def remove_stock(self, item_name, quantity):
        if item_name not in self.items or self.items[item_name] < quantity:
            print(f"Cannot remove {quantity} of '{item_name}': not enough stock")
            return
        self.items[item_name] -= quantity
        print(f"Removed {quantity} of '{item_name}'. Remaining: {self.items[item_name]}")
        self._check_low_stock(item_name)
 
    def _check_low_stock(self, item_name):
        if self.items[item_name] <= self.low_stock_threshold:
            print(f"  ⚠ Low stock alert: '{item_name}' has only {self.items[item_name]} left")
 
    def report(self):
        print("\nInventory Report:")
        for item, qty in self.items.items():
            status = "LOW" if qty <= self.low_stock_threshold else "OK"
            print(f"  {item}: {qty} ({status})")
 
 
if __name__ == "__main__":
    inventory = Inventory(low_stock_threshold=5)
 
    inventory.add_stock("Widgets", 20)
    inventory.add_stock("Gadgets", 8)
    inventory.remove_stock("Widgets", 12)
    inventory.remove_stock("Gadgets", 5)
    inventory.remove_stock("Gizmos", 1)  # doesn't exist yet
 
    inventory.report()