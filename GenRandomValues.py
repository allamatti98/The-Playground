#Generate random values between 0 and 1, then values between any range you specify.
#Then pick a string at random
import random
for i in range(9):
    print(random.random())

for i in range (9):
    print(random.randint(10,20))

cities = ['London', 'New York', 'Los Angeles']
for i in range(9):
    print(random.choice(cities))














'''
import random
#Print between 0 and 1
for i in range(9):
    print(random.random())

#Print a selected range
for i in range(9):
    print(random.randint(0,100))x

#Select a string at random
names = ["Dayan", "Raymond", "Vercetti"]
for i in range(9):
    print(random.choice(names))
'''