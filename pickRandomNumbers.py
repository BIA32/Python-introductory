import random

randomNumber=[]
number = 100
for i in range(number):
    randomNumber.append(random.randint(1,100))
print(randomNumber)

print ("This is the minimum number: ", min(randomNumber))
print ("This is the biggest number: ", max(randomNumber))