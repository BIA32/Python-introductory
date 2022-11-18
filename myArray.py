myArray=[12, 3, 4, 6, 8, 9, 43]

number = int(input("Enter the number: "))

result=False

for i in myArray:
    if (number==myArray[i]):
        result=True

print (result)