def simple_interest(p, r, t):
    
    si = (p*r*t)/100
    print("Simple Interest is:", si)
    return si
    
p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))   
t = float(input("Enter the time in years: "))

simple_interest(p, r, t)

total = p + simple_interest(p, r, t)
print("Total amount after interest is:", total)