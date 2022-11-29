def prime_number(n):
    c = 0
    for x in range(2, n):
        if n % x == 0:
            c = c + 1
    return c

n = int(input("Type a number, and if prime... then true: "))
if prime_number(n) == 0:
    print("True")
else:
    print("False")