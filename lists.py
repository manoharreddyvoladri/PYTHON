import random
n = input(" Enter the name of the friend by seperating them with the commas")
n1 = n.split(",")
x = len(n1)
n2 = random.randint(0, x)
print(n1[n2])
#input ::
#mike,jack,micheal,cavin,jaan,moni,mark,mike,james,bond,hero,villain
 
