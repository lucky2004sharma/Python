import os

# 1. Set the folder path you want to look at
# Note: '.' means your current folder. 
# You can change it to something like 'C:/Users/' if you want!
folder_path = '/ window c'

# 2. Get a list of everything inside that folder
everything = os.listdir(folder_path)

# 3. Loop through the list and print each item one by one
for item in everything:
    print(item)