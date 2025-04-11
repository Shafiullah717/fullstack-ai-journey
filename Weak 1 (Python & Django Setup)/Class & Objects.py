# print("Class and Objects in Python")

# OPP (object Orientd Programming) 
# Class & Object
# A class is a blueprint for creating objects
# Attributes and Metthods
# An object is a intense of class


# A Car Class
class Car:
    # Constructor: Initialize attributes when the object is created
    def __init__(self, make, model, year):
        self.make = make      # Attribute
        self.model = model    # Attribute
        self.year = year      # Attribute
        self.is_running = False  # Default attribute

    # Method: Action the car can perform
    def start_engine(self):
        self.is_running = True
        print(f"{self.make} {self.model}'s {self.year} engine is now running.")

    def stop_engine(self):
        self.is_running = False
        print(f"{self.make} {self.model}'s {self.year} engine has stopped.")

# Create objects (instances) of the Car class
my_car = Car("Tesla", "Model S", 2023)
dad_car = Car("Toyota", "Camry", 2020)
friend_car = Car("Toyota", "fortunure" , 2022)

# Use methods
# my_car.start_engine()
# dad_car.stop_engine()
# friend_car.start_engine()


# A Bank Class
class BankAccount:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner            # Attribute
        self.account_number = account_number  # Attribute
        self.balance = balance        # Attribute

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance} and account owner name is {self.owner}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance} and account number is {self.account_number}")
        else:
            print("Insufficient funds!")

    def check_balance(self):
        print(f"Balance: ${self.balance}")

# Create objects
alice_account = BankAccount("Alice", "ACC123", 1000)
bob_account = BankAccount("Bob", "ACC456", 1000)

# Use methods
alice_account.deposit(500)   
alice_account.withdraw(200)  
bob_account.check_balance()  