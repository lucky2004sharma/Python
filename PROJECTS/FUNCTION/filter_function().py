tasks = []
while True:
    action = input("Add(a) / Show(s) / Quit(q): ")
    if action == "a":
        tasks.append(input("Enter task: "))
    elif action == "s":
        print("Tasks:", tasks)
    elif action == "q":
        break