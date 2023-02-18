import random 
print('Here we I am to Genrate the Strong password')
chars = 'QWERTYUIOASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm!@#$%^&*()_+=-{}[]<>?/.,' 
n = int(input('Enter the no.of  password : '))
l = int(input('Length of the password: '))
print('\n Here is your New password: ')

for pwd in range(n):
    passwords= ' '

    for c in range(l):
        passwords += random.choice(chars)
        print(passwords)
