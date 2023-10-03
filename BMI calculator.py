print("Hello Buddies Welcome to BMI Calculator \n Enter the Name : ")
T =input(" ")
h = input("Height : ")
w = input("Weight:  ")
bmi = int(w) / float(h) **2
if bmi < 18.5:
    print(" under weight" )
elif  bmi > 18.5:
    if bmi <25:
        print("Normal Weight")
    elif bmi >25 :
        if bmi <30:
            print("Overweight")
        elif bmi > 30:
            print("obessedkk ")

print(f"{bmi} of BMI for you "+T )
