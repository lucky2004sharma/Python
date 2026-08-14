    # fahrenheit = (celsius * 9 / 5) + 32

print("Welcome to temperature converter")

def celcius_to_farenheit(celcius):
    farenheit = ( celcius * 9/5 ) + 32
    return farenheit

def farenheit_to_celcius(farenheit):
    celcius = ( farenheit - 32 ) * 5/9
    return celcius


farenheit = float(input("Enter the farenheit value: "))
celcius = float(input("Enter the celcius value: "))

print("What you want to convert ?")
print(" 1. Celcius to farenheit : ")
print(" 2. Farenheit to celcius : ")

choice = int(input("Please select the value 1 or 2: "))

if choice == 1:
    farenheit = celcius_to_farenheit(celcius)
elif choice == 2:
    celcius = farenheit_to_celcius(farenheit)

faren = celcius_to_farenheit(celcius)
celci = farenheit_to_celcius(farenheit)

print("The value of farenheit by celcius is : ", faren)
print("The value of celcius by farenheit is : ", celci)