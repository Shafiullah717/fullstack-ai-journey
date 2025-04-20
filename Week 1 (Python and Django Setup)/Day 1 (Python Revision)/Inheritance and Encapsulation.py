# print("Inheritance and Encapsulation in python")
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
# alice_savings = SavingsAccount("Alice", 1000)
# alice_savings.add_interest() 

#  Encapsulation restrict direct access to an object's internal data and exposes only what's necessary.

# private Attributes

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private attribute (double underscore)

    def get_age(self):    # Getter method
        return self.__age

    def set_age(self, age):  # Setter method (with validation)
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive!")

# alice = Person("Alice", 30)
# print(alice.get_age()) 
# # alice.set_age(-5)   
# Hayatullah = Person("Hayatullah", 17)
# print(Hayatullah.get_age())
# Hayatullah.set_age(18)
# print(Hayatullah.get_age())
# Shafiullah = Person("Shafiullah" , 22)
# print(Shafiullah.get_age())
# Shafiullah.__age = 31
# print(Shafiullah.__age)
# Ahsan = Ahsan.__age = 22
# print(Ahsan)

# Python's @property Decorator

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius  # Protected attribute

    @property
    def celsius(self):  # Getter
        return self._celsius

    @celsius.setter
    def celsius(self, value):  # Setter with validation
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):  # Computed property
        return (self._celsius * 9/5) + 32

temp = Temperature(25)
print(temp.fahrenheit)  
temp.celsius = 30       
temp.celsius = -200     
print(temp.celsius)
