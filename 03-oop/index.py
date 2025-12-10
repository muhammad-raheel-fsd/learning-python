# Object oriented programming
# 1-  Classes and Objects
class Character:
    # __init__ is a constructor
    # self is a reference to the current instance of the class
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, enemy):
        enemy.health -= self.power
        print(f"{self.name} attacks {enemy.name} for {self.power} damage.")
        if enemy.health <= 0:
            print(f"{enemy.name} is defeated!")


# Usage
hero = Character("Hero", 100, 20)
monster = Character("Monster", 80, 15)

hero.attack(monster)


# Inheritance
class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def start(self):
        print(f"{self.model} is starting.")

    def stop(self):
        print(f"{self.model} is stopping.")


ford = Car("Ford Mustang", 2020)
ford.start()
ford.stop()

bughatti = Car("Bugatti Chiron", 2021)
bughatti.start()
bughatti.stop()


class ElectricCar(Car):
    def __init__(self, model, year, battery_size):
        super().__init__(model, year)  # Call the constructor of the parent class
        self.battery_size = battery_size

    def charge(self):
        print(f"{self.model} is charging its {self.battery_size}-kWh battery.")


tesla = ElectricCar("Tesla Model S", 2022, 100)
tesla.start()
tesla.charge()
tesla.stop()

# Polymorphism - same method name, different implementations
# Simple example

print(1 + 2)  # Integer addition
print("Hello " + "World")  # String concatenation
print([1, 2] + [3, 4])  # List concatenation
print(len("Hello"))  # String length
print(len([1, 2, 3, 4, 5]))  # List length
print(len({"a": 1, "b": 2, "c": 3}))  # Dictionary length
print(len((10, 20, 30)))  # Tuple length


# OOP Polymorphism


class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        raise NotImplementedError("Subclasses must implement this method")


class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self) -> str:
        return f"{self.name} says Meow!"


class Cow(Animal):
    def speak(self) -> str:
        return f"{self.name} says Moo!"


# Polymorphism in action
animals = [
    Dog("Spike"),
    Cat("Whiskers"),
    Cow("Bessie"),
]

for animal in animals:
    print(animal.speak())  # Each one behaves differently, but same method is called


# encapsulation
class BankAccount:
    def __init__(self, account_number: str, balance: float = 0.0):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount:.2f}. New balance is ${self.__balance:.2f}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount: float) -> None:
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance is ${self.__balance:.2f}.")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self) -> float:
        return self.__balance

    def get_account_number(self) -> str:
        return self.__account_number

# Usage
account = BankAccount("123456789", 1000.0)
account.deposit(500.0)
account.withdraw(200.0)
print(f"Account Number: {account.get_account_number()}")
print(f"Current Balance: ${account.get_balance():.2f}")

#  Abstraction
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)
    
# Usage
rect = Rectangle(10, 5)
print(f"Area of rectangle: {rect.area()}")
print(f"Perimeter of rectangle: {rect.perimeter()}")    