current_balance = 100
amount = int(input ("how  much do you take? "))

def withdraw_money (current_balance, amount):
    if (current_balance >= amount):
        current_balance = current_balance - amount
        print ("sufficient funds")
        print ("current balance now: ", current_balance)
    else:
        print ("insufficient funds")

withdraw_money(current_balance,amount)


