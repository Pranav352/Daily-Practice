  ############################### Encapsulation ########################
# used for hiding data
# public, private, protected

class BankAcount:
    def __init__(self,balance):
        self.balance = balance

    def deposite(self,amount):
        self.balance += amount

    def show_balance(self):
        print(self.balance)

account = BankAcount(1000000)
account.deposite(540)
account.show_balance()

# Task 1
class ATM:
    def __init__(self,balance):
        self.balance = balance

    def widhrawl(self,amount):
        self.balance -= amount

    def show_balance(self):
        print(self.balance)
atm = ATM (20000000)
atm.widhrawl(50000)
atm.show_balance()

# Task 2: Student Marks System 🎓
# Create a class Student.
# Requirements:
# Private attributes:
# __name
# __marks
# Methods:
# set_marks(marks)
# get_marks()
# display_student()
# Condition:
# Marks must be 0–100 only.

class Student:
    def __init__(self,name):
        self.__name = name #private attribute
        self.__marks = 0    #private attribute

    def set_marks(self,marks):
        if marks >= 0 and marks <= 100:
            self.__marks = marks
        else:
            print("Marks should be between 0 to 100")
    
    def get_marks(self):
        return self.__marks
    
    def display_student(self):
        print("name:",self.__name)
        print("marks:", self.__marks)
#   create object    
s1 = Student("Rahul")

# set marks
s1.set_marks(54)

# display data
s1.display_student()





class car:
    def __init__(self,brand):
        self.brand = brand
c1 = car("BMW")
print(c1.brand)



         ####################### Inheritance ###########################
# parrent, chile class
# it has 5 types "Single, Multiple, Multilevel, Hirechical, Hybrid"

class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")
d1 = Dog()

d1.eat()
d1.bark()

# Task 1: Vehicle → Car
# Parent Class: Vehicle
# Attribute: brand
# Method: start() → prints "Vehicle is starting"
# Child Class: Car
# Method: drive() → prints "Car is driving"
# Goal: Create a Car object, call both start() and drive() methods.

class vehical:
    def __init__(self,brand):
        self.barnd = brand

    def start(self):
            print("vehical is starting")

class car(vehical):
    def drive(self):
        print("car is driving")

c = car("BMW")
c.start()
c.drive()

# Task 2: Person → Employee
# Parent Class: Person
# Attributes: name, age
# Method: display_person() → prints name and age
# Child Class: Employee
# Attribute: salary
# Method: display_employee() → prints name, age, and salary
# Goal: Create an Employee object, show all details.

# Parent Class
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display_person(self):
        print("name",self.name)
        print("Age",self.age)

# Child Class
class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary =salary

    def display_employee(self):
        self.display_person()
        print("Salary",self.salary)
# create obj of employee
emp1 = Employee("Rahul",24, 24000)

# display all details
emp1.display_employee()

# Task 5: BankAccount → SavingsAccount
# Parent Class: BankAccount
# Attribute: balance
# Method: deposit(amount) → adds money
# Child Class: SavingsAccount
# Method: withdraw(amount) → subtracts money if balance is enough
# Goal: Create a SavingsAccount, deposit money, withdraw money, print balance.

# Parent Class
class BankAccount:
    def __init__(self):
        self.balance = 0
    def deposite(self,amount):
        if amount > 0:
            self.balance += amount
            print("Deposite",amount)
        else:
            print("Deposite amount must be positive")
# Child Class
class SvaingAccount(BankAccount):
    def withdraw(self,amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print("withdraw amount ", amount)
            else:
                print("Insufficient balance")
        else:
            print("withdraw amount must be positive")
# create obj of saving account        
my_acc = SvaingAccount()

# Deposite money
my_acc.deposite(10000)

# withdraw money
my_acc.withdraw(5000)

# print remaining  balance
print("Current balance",my_acc.balance)


          ########################### Polymorphism ############################
# Same funtion name but differnt behavior

# polymorphism with method (Method Overriding)
# polymorphism with operator (Method Overloading)

# method overriding

class Animal:
    def speak(self):
        print("Animal make a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")
        
class Cat(Animal):
    def speak(self):
        print("cat meow")
# objects
a = Animal()
d = Dog()
c = Cat()

# call speak method
a.speak()
d.speak()
c.speak()

# method overloding directly not support in python


             ##################### Abstraction ######################
from abc import ABC , abstractmethod

class Vehical(ABC): #Abstract Class
    def __init__(self,brand):
        self.brand = brand
        
    
    @abstractmethod
    def start(self):
        pass

class Car(vehical):
    def start(self):
        print(self.barnd,"car Open  with key :")

class Bike(vehical):
    def start(self):
        print(self.barnd,"Bike Start with key :")

# create object
p = Car("toyota")
r = Bike("pulsar")

p.start()
r.start()


class Employee(ABC):
    def __init__(self,position):
        self.position = position

    @abstractmethod
    def emp(self):
        pass

class Managar(Employee):
    def emp(self):
        print(self.position,"Manager handle Workload :")

class Developer(Employee):
    def emp(self):
        print(self.position,"Developer develop the project : ")

M = Managar("Pradip")
D = Developer("Rahul")

M.emp()
D.emp()

# Task 1
# Payment System
# Create an abstract class Payment with method pay().
# Child classes:
# CreditCard
# UPI
# Cash
# Each class prints a different payment message.
# Example output:

# Payment done using Credit Card
# Payment done using UPI
# Payment done using Cash
class Payment_system(ABC):

    @abstractmethod
    def pay():
        pass
class CreditCard(Payment_system):
    def pay(self):
        print("Payment done using Credit Card : ")

class UPI(Payment_system):
    def pay(self):
        print("Payment done using UPI :")

class Cash(Payment_system):
    def pay(self):
        print("Payment done using Cash:")

C = CreditCard()
U = UPI()
CA = Cash()

C.pay()
U.pay()
CA.pay()

# Task 2
# Login Authentication System
# Create abstract class Login with method authenticate().
# Child classes:
# GoogleLogin
# FacebookLogin
# EmailLogin
# Each class prints different authentication message.

class Login(ABC):
    def __init__(self,system):
        self.system = system

    @abstractmethod
    def authenticate(self):
        pass
class GoogleLogin(Login):
    def authenticate(self):
        print(self.system ,": success login using your google account:")
class FacebookLogin(Login):
    def authenticate(self):
        print(self.system,": FaceBook login sucess:")
class EmailLogin(Login):
    def authenticate(self):
        print(self.system,": Emial authenticate succesfully:")

G = GoogleLogin("GOOGLE")
F = FacebookLogin("FACEBOOK")
E = EmailLogin("EMAIL")

G.authenticate()
F.authenticate()
E.authenticate()

# Task 3
# Food Ordering System
# Create an abstract class FoodOrder with method prepare_food().
# Child classes:
# Pizza
# Burger
# Pasta
# Each class prints how the food is prepared.

class FoodOrder(ABC):

    @abstractmethod
    def prepare_food():
        pass
class pizza(FoodOrder):
    def prepare_food(self):
        print("Pizza is baking")
class Burger(FoodOrder):
    def prepare_food(self):
        print("burger is in oven to grild")
class Pasta(FoodOrder):
    def prepare_food(self):
        print("pasta is preparing")
pi = pizza()
bu = Burger()
pa = Pasta()

pi.prepare_food()
bu.prepare_food()
pa.prepare_food()

# Task 4
# Notification System
# Create an abstract class Notification with method send().
# Child classes:
# EmailNotification
# SMSNotification
# PushNotification

class Notification(ABC):

    @abstractmethod
    def send():
        pass
class EmailNotifaction(Notification):
    def send(self):
        print("EmailNotification sent successfully")
class SMSNotifaction(Notification):
    def send (self):
        print("SMS notification sent successfully")
class PushNotification(Notification):
    def send(self):
        print("Pushnotification sent successfully")

Em = EmailNotifaction()
SM = SMSNotifaction()
pu = PushNotification()

Em.send()
SM.send()
pu.send()

# Task 5 Login Security System
# Create an abstract class SecuritySystem with method verify().
# Child classes:
# Fingerprint
# FaceRecognition
# Password
# Each class prints a different verification process.

class SecuritySystem(ABC):

    @abstractmethod
    def verify(self):
        pass

class Fingerprint(SecuritySystem):
    def verify(self):
        print(" Fingerprint verification process")

class FaceRecognition(SecuritySystem):
    def verify(self):
        print(" Facerecognition verification process")
class Passsword(SecuritySystem):
    def verify(self):
        print(" Password verification process")
finger_print = Fingerprint()
face_recognition = FaceRecognition()
pasword = Passsword()

finger_print.verify()
face_recognition.verify()
pasword.verify()



class Bank(ABC):
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    @abstractmethod
    def calculate_interest(self):
        pass

class SavingsAccount(Bank):
    def calculate_interest(self):
        interest = self.balance * 0.04
        print(f"Savings Interest for {self.account_holder}: {interest}")

class CurrentAccount(Bank):
    def calculate_interest(self):
        interest = self.balance * 0.01
        print(f"Current Interest for {self.account_holder}: {interest}")

# Objects
sav = SavingsAccount("Alice", 10000)
curr = CurrentAccount("Bob", 20000)

sav.calculate_interest()
curr.calculate_interest()


