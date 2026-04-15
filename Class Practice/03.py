def deposite(balance, amount = 100):
    balance += amount
    print("The updated balance is:", balance)
    
def withdraw(balance, amount):
    if amount > balance:
        print("Insufficient Balance")
    else:
        balance -= amount
    
    print("Your updated balance is:", balance)
    
    
deposite(12000, 500)
withdraw(12000, 4000)