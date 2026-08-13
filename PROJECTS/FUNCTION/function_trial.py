# ==========================
#        THE GYM
# ==========================

print("========== THE GYM ==========")


# -----------------------------
# User Details Function
# -----------------------------
def user_details():
    name = input("Please Enter your Name : ")
    age = int(input("Please Enter your Age : "))
    return name, age


# -----------------------------
# Membership Function
# -----------------------------
def membership():

    print("\nAvailable Memberships")
    print("1. Basic    = ₹1000")
    print("2. Premium  = ₹2000")
    print("3. VIP      = ₹3000")

    choose = int(input("\nChoose Membership : "))

    if choose == 1:

        membership_name = "Basic Membership"
        membership_fee = 1000
        discount_percent = 10

    elif choose == 2:

        membership_name = "Premium Membership"
        membership_fee = 2000
        discount_percent = 15

    elif choose == 3:

        membership_name = "VIP Membership"
        membership_fee = 3000
        discount_percent = 20

    else:
        print("Invalid Choice")
        return None

    membership_discount = membership_fee * discount_percent / 100

    after_discount = membership_fee - membership_discount

    return (membership_name,
            membership_fee,
            discount_percent,
            membership_discount,
            after_discount)


# -----------------------------
# Age Discount Function
# -----------------------------
def age_discount(age, after_discount):

    extra_discount = 0
    message = "No Extra Discount"

    if 18 <= age <= 25:

        extra_discount = after_discount * 5 / 100
        message = "Student Discount (5%)"

    elif age > 60:

        extra_discount = after_discount * 7 / 100
        message = "Senior Citizen Discount (7%)"

    final_amount = after_discount - extra_discount

    return final_amount, extra_discount, message


# -----------------------------
# Receipt Function
# -----------------------------
def receipt(name,
            age,
            membership_name,
            membership_fee,
            discount_percent,
            membership_discount,
            message,
            extra_discount,
            final_amount):

    print("\n========== FINAL RECEIPT ==========")

    print("Name                 :", name)
    print("Age                  :", age)
    print("Membership           :", membership_name)
    print("Original Fees        : ₹", membership_fee)

    print("Membership Discount  :", str(discount_percent) + "%")
    print("Discount Amount      : ₹", membership_discount)

    if extra_discount > 0:
        print(message)
        print("Extra Discount       : ₹", extra_discount)

    print("--------------------------------------")
    print("Final Amount         : ₹", final_amount)
    print("======================================")


# -----------------------------
# Main Function
# -----------------------------
def main():

    # User Details
    name, age = user_details()

    # Membership Details
    data = membership()

    if data == None:
        return

    (membership_name,
     membership_fee,
     discount_percent,
     membership_discount,
     after_discount) = data

    # Age Discount
    final_amount, extra_discount, message = age_discount(age, after_discount)

    # Final Receipt
    receipt(name,
            age,
            membership_name,
            membership_fee,
            discount_percent,
            membership_discount,
            message,
            extra_discount,
            final_amount)


# Program Starts Here
main()