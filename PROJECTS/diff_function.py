class UPI:

    def pay(self):
        print("Payment through UPI")


class CreditCard:

    def pay(self):
        print("Payment through Credit Card")


class Cash:

    def pay(self):
        print("Payment through Cash")


payments = [UPI(), CreditCard(), Cash()]

for payment in payments:
    payment.pay()