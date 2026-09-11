notes = []

while True:
    print("\n1. Add Note")
    print("2. Show Notes")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        note = input("Write note: ")
        notes.append(note)

    elif choice == "2":
        for note in notes:
            print("-", note)

    elif choice == "3":
        break