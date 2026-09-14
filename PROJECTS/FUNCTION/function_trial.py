log = []
while True:
    entry = input("How's your day going? (emoji or 'exit'): ")
    if entry == "exit":
        break
    log.append(entry)

print("\nYour mood journey today:")
print(" ➡ ".join(log) if log else "No entries logged.")