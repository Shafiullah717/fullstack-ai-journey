print("Inheritance and Encapsulation in python")
# Inheritance allow a child class to inherit attributes and metthods for the parent class.

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Child class inheriting from Animal
class Dog(Animal):
    # Override the parent's speak() method
    def speak(self):
        print(f"{self.name} barks: Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows: Meow!")
class Goat(Animal):
    def speak(self):
        print(f"{self.name} bleat: main! ")        

# Create objects
dog = Dog("Buddy")
cat = Cat("Whiskers")
goat = Goat("Lilly")

# dog.speak()  
# cat.speak()  
# goat.speak()

# Inheritance also increase Functionality

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Balance: ${self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner, balance)  # Call parent's __init__
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)  # Reuse parent's deposit() method

# Create a savings account
alice_savings = SavingsAccount("Alice", 1000)
alice_savings.add_interest() 