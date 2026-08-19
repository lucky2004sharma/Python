class TodoList:
    def __init__(self):
        self.tasks = []
 
    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        print(f"Added: {task}")
 
    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
            print(f"Completed: {self.tasks[index]['task']}")
        else:
            print("Invalid task index")
 
    def show_tasks(self):
        for i, t in enumerate(self.tasks):
            status = "✔" if t["done"] else "✗"
            print(f"[{status}] {i}: {t['task']}")
 
 
if __name__ == "__main__":
    todo = TodoList()
    todo.add_task("Buy groceries")
    todo.add_task("Finish Python project")
    todo.add_task("Read a book")
    todo.complete_task(1)
    print("\nCurrent tasks:")
    todo.show_tasks()