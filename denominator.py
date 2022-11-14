num1 = int(input("Please enter your 1st number: "))

num2 = int(input("Please enter your 2nd number: "))
def comDenominator(num1, num2):
    small=True

    comDenominatorArray=[]

    if (num1<num2):
        small = num1
    else:
        small = num2

    for i in range (1,small):
         if (num1 % i == 0 and num2 % i == 0):
             print("Common Denominator: ", i)
             comDenominatorArray.append(i)

    return (comDenominatorArray)

comDenominator(num1, num2)