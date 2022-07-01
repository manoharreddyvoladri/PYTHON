import random 
while True:     
     print('''1. Roll the dice \n''')
     print('''2. Exit''')    
     num = int(input("what you want to do\n"))     
     if num==1:         
        number = random.randint(1,6)         
        print(number)     
     else:
        break
