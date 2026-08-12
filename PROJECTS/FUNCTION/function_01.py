# def discount_price(price, discount):
    
#     print("The price is : ", price)
#     print("The discount is : ", discount)
#     discount_val = (price*discount)/100
#     discount_prince = price - discount_val
    
#     return discount_prince

    
# def gst_value(price):
    
#     gst = price * 18 /100
#     gst_valu = price + gst
#     print("The price after Gst is : ", gst_valu)
       
#     return gst_valu
    
    
# price = 200
# after_gst = gst_value(price)
# after_discount = discount_price(price, 10)


# print(price)
# print(after_gst)
# print(after_discount)



def discount_price(price1, discount):
    
    discount_va =(price1 * discount)/100
    discount_pric = price1 - discount_va
    return discount_pric


def gst_value(price1):
    
    gst = (price1 * 18)/100
    gst_price = price1 + gst
    return gst_price

price1 = int(input("The overall price is : "))
after_gst = gst_value(price1)
after_discount = discount_price(price1, 10)

print(price1)
print(after_gst)
print(after_discount)

