username = "admin"
password = "1234"

user = input("Username: ")
passcode = input("Password: ")

if user == username and passcode == password:
    print("Login successful!")
else:
    print("Wrong username or password")