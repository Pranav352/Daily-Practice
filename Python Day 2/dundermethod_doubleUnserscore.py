# these are the method of Dunder method it means double underscore
# __init__
# __str__
# __len__
# __add__
# __eq__

class Book:
    def __init__(self,title,pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"Book: {self.title}" #print method " f "
    
    def __len__(self):
        return self.pages
    
    def __eq__(self,other):
        return self.pages == other.pages
    
b1 = Book("Python",240)
b2 = Book("Java",440)

print(b1) #__str__
print(len(b1)) #__len__
print(b1 == b2) #__eq__


# EX for __add__

class Number:
    def __init__(self,value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)
v1 = Number(10)
v2 = Number(20)

result = (v1 + v2)

print(result.value)



# Task 1
# Bank Account
# Dunder methods used
# __init__
# __str__
# __add__
# __eq__
# Idea
# Create a BankAccount class.
# Features:
# Store owner and balance
# Print account details
# Add two accounts
# Compare balances

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Bank Account Owner: {self.owner}\n Bank Account Balance: {self.balance}"
    
    def __add__(self, other):
        return  self.balance + other.balance
    
    def __eq__(self, others):
        return  self.balance == others.balance
    
bank1 = BankAccount("Jon",5000)
bank2 = BankAccount("Ram",4000)

print(bank1)
print(bank1 + bank2)
print(bank1 == bank2)

    


