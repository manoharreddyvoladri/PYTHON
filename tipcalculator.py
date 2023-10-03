b=float(input("Enter the the bill amount? "))
t= int(input(" Enter the percent of tip you Want to pay ? "))
ta = (t/100)*b + b
p =int(input(" No.of splits ? "))
print(f"The total amount is {ta}")
tbp = ta/p
tb = "{:.2f}".format(tbp)
print(f" Split for the Each person {tb}")
