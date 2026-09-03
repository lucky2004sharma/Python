marks = [10,15,20,25,30]
bonus = [1,2,3,4,5]
bonus1 = [10,20]

def number(num1, num2,num3):
    return num1 , num2 , num3
    print(num1, num2, num3)
filtered_numbers = map(number, marks, bonus, bonus1)
# print(list(filtered_numbers)) # print the square of each number in the list
for element in filtered_numbers:
    print(element)