print ("How much would you like to withdraw?")

def withdraw_money (current_balance, amount):
    if (current_balance >= amount):
        current_balance = current_balance - amount
    print ("insufficient funds")
current_balance = 100

withdraw_money = input ("")

if withdraw_money <= current_balance:
    print ("Here is your money")
else:
    print ("insufficient funds")