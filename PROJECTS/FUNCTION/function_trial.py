# def addition(num1, num2):
#     return num1 + num2

# # addition(10,20)
# print(addition(10,20))

def addition(*nums):
    sum = 0
    for n in nums:
        sum = sum + n 
    print(sum)
    return sum

addition(10,20,30)
addition(10,20,30,40,50,60)