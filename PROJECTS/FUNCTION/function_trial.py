# def addition(num1, num2):
#     return num1 + num2

# # addition(10,20)
# print(addition(10,20))


# variable length positional arguments.
# def addition(*nums):
#     sum = 0
#     for n in nums:
#         sum = sum + n 
#     print(sum)
#     return sum

# addition(10,20,30)
# addition(10,20,30,40,50,60)

# variable length keyword argumengs.

def addition(**nums):
    print(nums)
    print(type(nums))
    return sum(nums.values())

addition(a=20, b=30, c=40)
print(addition(a=10,b=20,c=30,d=40))