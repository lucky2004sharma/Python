hours = int(input("Hours until your deadline: "))
minutes = hours * 60
messages = {
    0: "It's already here — go!",
    60: "Only an hour, hustle!",
    180: "A few hours, stay focused!",
}
closest = min(messages.keys(), key=lambda x: abs(x - minutes))
print(f"You have {minutes} minutes left. {messages[closest]}")