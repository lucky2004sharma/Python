'''# checking vowels and consonants in a string


name = input("Enter your name: ")
vowels = ['a', 'e', 'i', 'o', 'u']

def vowels_count(name):
    if name in  vowels:
        return True
    else:
        return False
    
filtered_name = filter(vowels_count, name)
print(list(filtered_name))'''

# by lambda function

name = input("Enter your name : ")
vowels = ['a', 'e', 'i', 'o', 'u']

filtered_name = filter( lambda name : name in vowels, name)
print(list(filtered_name))

