# OOP concepts
# CLASS
class person:
    pass
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = person("rahul",22)
print(p1.name)


class person:
    species = "human"  ##Class variable

    def __init__(self,name,age):
        self.name = name #instance variable
        self.age = age
# ✔Class variable → shared by all objects
# ✔ Instance variable → different for each object


class people:
    def role(self):
        return "i am person"
class employee:
    def role(staf):
        return "i am an employe"   
    
class student:

    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def display(self):
        print("name:", self.name)
        print("age:", self.age)
s1 = student("Rahul",21)
s1.display()

# Task 1 Class: Car
# Attributes: brand, model, price
# Method: show_details()

class car:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
        
    def show_details(self):
        print("brand:",self.brand)
        print("model:",self.model)
        print("price:",self.price)

gaddi = car("BMW","X7",30000000)
gaddi.show_details()


# Task 2 Class: Book
# Attributes: title, author, price
# Method: display_book()
class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def display_book(self):
        print("title:",self.title)
        print("author:",self.author)
        print("price:",self.price)
book = Book("ninja","premanad",240)
book.display_book()


# Task 3 Class: Employee
# Attributes: name, salary
# Method: show_salary()

class employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def show_salary(self):
        print("name:",self.name)
        print("salary:",self.salary)
emp = employee("Herry",24000)
emp.show_salary()

class showroom:
    def __init__(self,cars,employee,):
        self.cars = cars
        self.employee = employee

    def show_revenue(self):
        print("cars:",self.cars)
        print("employee:",self.employee)
show = showroom("branded",240)
show.show_revenue()



    