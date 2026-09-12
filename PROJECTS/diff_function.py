text = input("Enter your text: ")
word = input("What word do you want to find? ")

if word.lower() in text.lower():
    print("Word found!")
else:
    print("Word not found!")