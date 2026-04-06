from abc import ABC, abstractmethod

# Abstract Parent class
class Account(ABC):
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance # encapsulated. hide balance data

    @abstractmethod
    def deposite(self,amount):
        pass

    @abstractmethod
    def withdraw(self,amount):
        pass

    def get_balance(self):
        return self.__balance
    
    def _update_balance(self,amount):
        self.__balance += amount

    def __str__(self):
        return f"account {self.name} balance {self.__balance}"
        
# Saving Account

class SavingAccount(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance)



    def deposite(self,amount):
        print("Deposite",amount,"to saving account")
        self._update_balance(amount)

    def withdraw(self,amount):
        if amount > self.get_balance():
            print("Insefficiant balance in account")
        else:
            print("withdraw",amount,"from saving account")
            self._update_balance( - amount)
    
# current Account
class CurrentAccount(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance)

    def deposite(self,amount):
        print("deposite",amount,"to current account")
        self._update_balance(amount)

    def withdraw(self,amount):
        print("withdraw",amount,"from current account")
        self._update_balance(-amount)

# operator overlodding : add balance of two account

def add_accounts(ac1,ac2):
    
    return ac1.get_balance() + ac2.get_balance()

# Create objects

saving = SavingAccount("Bob",5000)
current = CurrentAccount("prem",2000)

saving.deposite(10000)
saving.withdraw(5000)
current.deposite(10000)
current.withdraw(5000)

print(saving)
print(current)

print("Total balance",add_accounts(saving,current))



# Mega Project
# Bank, ATM, Library
# BANK
class Bank(ABC):
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance # encapsulated
    
    def get_balance(self):
        return self.__balance
    def update_balance(self,amount):
        self.__balance = amount

    @abstractmethod
    def withdrw(self,amount):
        pass

    def deposite(self,amount):
        self.update_balance(amount)

class SavingAccount(Bank):

    def withdrw(self, amount):
        if amount > self.get_balance():
            print("Insufficiant Balance")
        else:
            self.update_balance(-amount)
            print("withdrawl successfull")

class CurrentAccount(Bank):
    def withdrw(self, amount):
        self.update_balance(-amount)
        print("withdrawl successfull")

# ATM
class ATM:
    def __init__(self,account,pin):
        self.account = account
        self.pin = pin


    def authenticate(self):
        p = input("Enter your pin:")
        return p == self.pin
    
    def menu(self):
        if not self.authenticate():
            print("Invalid pin")
            return
        
        while True:

            print("\n ATM Menue")
            print("1.Check Balance")
            print("2.Deposite")
            print("3.Withdraw")
            print("4.Exit")

            ch = input("Enter your choice:")

            if ch == "1":
                print("Balance:",self.account.get_balance())
            elif ch == "2":
                amount = int(input("Enter amount to deposite:"))
                self.account.deposite
            elif ch == "3":
                amount = int(input("Enter amount to withdraw:"))
                self.account.withdraw(amount)
            elif ch == "4":
                break
            else:
                print("Invalid choice")

# Library
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.issued = False


    def __str__(self):
        status = "Issued" if self.issued else "Available"
        return self.title - self.author , status
class Library:
    def __init__(self):
        self.books = []

    def add_book(self,title,author):
        self.book.append(Book(title,author))

    def show_books(self):
        if not self.books:
            print("No books avaliable")
            return
        for i,b in enumerate(self.book):
            print(i+1,b)
    