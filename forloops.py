Students=("Melh, samuel, Ben, Memet")

even_numbers = [ ]
odd_numbers = [ ]

for studentsName in Students:
    print (studentsName)

for number in range (10, 100):
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)
    print (number)