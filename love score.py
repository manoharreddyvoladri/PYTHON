print("love calculator")
n1 =input(" Enter your name " )
n2 = input("Enter your crush name")
cn12 = n1 +n2
lcn = cn12.lower()
t = lcn.count("t")
r = lcn.count("r")
u = lcn.count("u")
e = lcn.count("e")
a = t+r+u+e
l = lcn.count("l")
o = lcn.count("o")
v = lcn.count("v")
e = lcn.count("e")
b =  l+o+v+e
nl = str (a) + str (b)
tl = int(nl)
if tl >100:
    print("You both made for each other :)")
elif ( tl > 50 ) or (tl <90):
    print(f" Your love score is {tl}, you both like coke aand mentos")
elif (tl >10) or (tl<50):
    print(f" Your love score is {tl}, you both guys stay like the  kushi")

