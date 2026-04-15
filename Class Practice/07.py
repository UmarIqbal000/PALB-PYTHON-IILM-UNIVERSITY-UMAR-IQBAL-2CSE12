# User have create two methods deposite and wothdraw in a class account for various objects

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposite(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
            
# Example usage
account1 = Account("Alice", 1000)
account1.deposite(500)  # Deposited 500. New balance: 1500
account1.withdraw(200)   # Withdrew 200. New balance: 130