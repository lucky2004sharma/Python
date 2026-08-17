def main():
    todo_list = []
    
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View Tasks")
        print("2. Add a Task")
        print("3. Remove a Task")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            if not todo_list:
                print("\nYour list is empty!")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(todo_list, 1):
                    print(f"{i}. {task}")
        elif choice == '2':
            task = input("\nEnter the new task: ")
            todo_list.append(task)
            print("Task added!")
        elif choice == '3':
            try:
                task_num = int(input("\nEnter task number to remove: "))
                if 1 <= task_num <= len(todo_list):
                    removed = todo_list.pop(task_num - 1)
                    print(f"Removed: '{removed}'")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()