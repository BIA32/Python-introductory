print = int(input("Choose how many numbers you want to add up for fibonacci: "))

def fibonacci(n):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2, n):
        print(a+b)
        a, b = b, a + b

if 