# User have create two methods deposite and wothdraw in a class account for various objects

class Account:
    def __init__(self, balance):
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            
    def display(self):
        print(self.balance)
        
obj1 = Account(1000) 
print(obj1.balance)  
obj1.deposit(500)#Output: 1000
print(obj1.balance)
obj1.display()

obj1.withdraw(500)
print(obj1.balance)