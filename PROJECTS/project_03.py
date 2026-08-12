print("THIS IS MY 3RD PROJECT")

print("Hello! Welcome to Grocery Store")

user_name = input("Please! Enter your name :")

rice_price = int(input("Enter the rice price :"))
milk_price = int(input("Enter the milk price :"))
bread_price = int(input("Enter the bread price :"))
rice_quantity = int(input("Enter the rice quantity :"))
milk_quantity = int(input("Enter the milk quantity :"))
bread_quantity = int(input("Enter the bread quantity :"))


rice_total = rice_price*rice_quantity
milk_total = milk_price*milk_quantity
bread_total = bread_price*bread_quantity

total_bill = rice_total + milk_total + bread_total

if total_bill >= 500:
    discount = (total_bill * 10)/100

else:
    discount = 0
    print("NO Discount")

    
final_bill = total_bill - discount
print("------- FINAL BILL -------")




print("Customer name :", user_name)
print("Rice Total :", rice_total)
print('Milk Total :', milk_total)
print("Bread Total :", bread_total)
print("Total bill :", total_bill)
print("Discont ", discount)
print("Final bill :", final_bill)

print("Thank You For Shopping!")





