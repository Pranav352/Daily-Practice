# ex of all oops

# encapsulation
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance #data is hiding using __balance

    def get_balance(self):
        return self.__balance
df = BankAccount(5000)
print(df.get_balance())


class ATM:
    def __init__(self,bank):
        self.__bank = bank  #data is hiding using __bank


    def get_money(self):
        return self.__bank
atm = ATM(50000)
print(atm.get_money())   


# Inheritance

class Animal:   # parent class
    def eat(self):
        print("Animal eating:")

class Dog(Animal): # child class
    def bark(self):
        print("Dog barking:")
d = Dog()
d.eat()
d.bark()


class Tata:
    def rangerover(self):
        print("laxuary brand:")
class nexon(Tata):
    def heriar(self):
        print("Harrier is a SUV")
n = nexon()
n.rangerover()
n.heriar


# polimorphisam
class cars:
    def sound(self):
        print("cars are running")

class BMW(cars):
    def sound(self):
        print("BMW is a brand")

class TATA(cars):
    def sound(self):
        print("Tata is solid")

# for cars in (BMW(),TATA()):
#     cars.sound

# object
a = cars()
f = BMW()
g = TATA()

# call sound method
a.sound()
f.sound()
g.sound()


class animal:
    def speak(self):
        print("animal speaking")

class dog(animal):
    def speak(self):
        print("dog is barking")

class cat(animal):
    def speak(self):
        print("cat is meowing")
# objects
A = animal()
D = dog()
C = cat()

# cal sound method
A.speak()
D.speak()
C.speak()





