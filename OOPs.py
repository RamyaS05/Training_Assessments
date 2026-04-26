
#section1: class, Object, Self
#t1 and t2:Create a class called "Student" with attributes "name" and "age". Include a method to display the student's information. 
from abc import ABC, abstractmethod


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}\n")
student1=Student("Ramya", 21)
student2=Student("pree",25)
student1.display()
student2.display()

#t3 : create a class rectangle with attributes length and width. Include a method to calculate the area
class Rectangle:
    def __init__(self,length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
rect=Rectangle(5, 3)
print(rect.area())

#t4: Create a class called "Car" with attributes "brand" and "price" and use a method to display the car's details
class Car:
    def __init__(self,brand, price):
        self.brand = brand
        self.price = price
    def method(self):
        print(f"\nbrand:{self.brand}, price:{self.price}\n")
c1=Car("Toyota", 200000)
c1.method()

#section 2: constructor and instance variables
#t5 & t6: Create a class called "Employee" with constructor to initialize the employee's name and salary. Include a method to increase the salary by a certain percentage.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def increase_salary(self, percentage):
        self.salary += self.salary * (percentage / 100)
employee1 = Employee("Ramya", 20000)
employee1.increase_salary(10)
print(f"Name: {employee1.name}, Salary: {employee1.salary}\n")

#t7: Create a class called "Circle" with an attribute "radius" and a method to calculate the circumference.
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def circumference(self):
        return 2 * 3.14 * self.radius
c1=Circle(5)
print(c1.circumference())

#section 3: encapsulation
#t8, t9,t10: Create a class called "BankAccount" with a private attribute "balance". Include methods to deposit, withdraw and get the balance. 
class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance
    def deposit(self, amount):
            if amount > 0:
                self.__balance += amount
                return f"\nDeposited: {amount}"
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrawn: {amount}"
        else:
            print("Insufficient balance")
    def get_balance(self):
        return self.__balance
account = BankAccount(1000)
print(account.deposit(500))
print(account.withdraw(200))
print(f"current balance:{account.get_balance()}\n")

#section 4 & 5: Inheritance and Polymorphism
#t11, t12, t13, t14: Create a base class called "Animal" with a method "sound". Create two derived classes "Dog" and "Cat" that inherit from the "Animal" class and override the "sound" method.
class Animal:
    def sound(self):
        return "Animal speaks"
class Dog(Animal):
    def sound(self):
        return "dog barks"
class Cat(Animal):
    def sound(self):
        return "cat meows"
d=Dog()
c=Cat()
print(d.sound())
print(c.sound())


#t15: Create a base class called "Shape" with a method "area". Create two derived classes "Square" and "Triangle" and override it.
class Shape:
    def area(self):
        pass
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
square1=Square(4)
triangle1=Triangle(4, 5)  
print(f"\nArea of square: {square1.area()}")
print(f"Area of triangle: {triangle1.area()}\n")  

#Section 6: Abstraction
#t16 & t17: Create an abstract class called "Vehicle" with an abstract method "start" and create two derived classes "Car" and "Bike" that implement the "start" method.
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Bike(Vehicle):
    def start(self):
        return "Bike starts with a kick"
class Car(Vehicle):
    def start(self):
        return "Car starts with a push button"
bike = Bike()
car = Car()
print(bike.start())
print(car.start())
print("\n")

#Section 7: Class Variables and methods
#t18 & t19: Create a class Company with class variable "company_name" and class method to change company name.
class Company:
    company_name = "tech1"
    @classmethod
    def change_company_name(cls,new_name):
        cls.company_name= new_name
Company.change_company_name("tech2")
print(f"company name: {Company.company_name}\n")

#Section 8: Mini Project
#task 20: Create a class "library" with attributes as list of books and methods.
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"Book added: '{book_name}'")
    def remove_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"Book removed: '{book_name}'")
        else:
            print(f"Error: '{book_name}' is not in the library.")
    def show_books(self):
        if self.books:
            print("\nCurrent Library Collection:")
            for index, book in enumerate(self.books, 1):
                print(f"{index}. {book}")
        else:
            print("\nThe library is currently empty.")
my_lib = Library()
my_lib.add_book("The Alchemist")
my_lib.add_book("Atomic Habits")
my_lib.show_books()
my_lib.remove_book("The Alchemist")
my_lib.show_books()