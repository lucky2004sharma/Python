water = 0

while water < 8:
    glass = input("Did you drink a glass? (yes/no): ")

    if glass == "yes":
        water += 1
        print("Glasses:", water)

print("Daily water goal completed!")