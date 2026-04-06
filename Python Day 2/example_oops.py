# ex of all oops

# en
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance #data is hiding using __balance

    def get_balance(self):
        return self.__balance
df = BankAccount(5000)
print(df.get_balance())

# In

class Animal:   # parent class
    def eat(self):
        print("Animal eating:")

class Dog(Animal): # child class
    def bark(self):
        print("Dog barking:")
d = Dog()
d.eat()
d.bark()


# po
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
