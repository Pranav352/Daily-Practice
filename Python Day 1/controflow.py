# Condation Statment

age = 18

if age > 18:
    print("you are an adult")
else:
    print("you are minor")


value = 25000
if value > 30000:
    print("your order conform")
elif value >= 25000:
    print("your order processing")
else:
    print("your oder dely")


marks = 95

if marks >= 95:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 55:
    print("Grade C")
else:
    print("you are not clear")    


# Nested Condations

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("you can enter")
    else:
        print("ID required")
else:
    print("you are under age")   


# ATM withdrawl
Bank_Balance = 50000
Withdrawal_amount = 10000
pin_correct = True

if pin_correct:
    if Withdrawal_amount <= Bank_Balance:
        print("withdraw successfull")
        Bank_Balance -= Withdrawal_amount
        print("Remaining balance:",Bank_Balance)
    else:
        print("In sufficiant balance")
else:
    print("Incorrect pin")

# Login system
UserName = "Admin"
Password = "1234"

if UserName == "Admin":
    if Password == "1234":
        print("Login Successfully:")
        print("Access granted: Admin")
    else:
        print("Incorrect Password")
else:
    print("Username Mismatch")

# Ecommerce Disscounts
Bill_amount = 20000
is_member = True

if Bill_amount >= 20000:
    if is_member:
        discount = 0.20
        print("you get 20% discount")
    else:
        discount = 0.10
        print("you get 10%")
else:
    print("No discount available")


# Movie ticket
age = 12
is_weekend = True

if age < 12:
    print("ticket type:child")
    price = 100
    if is_weekend:
        price = price + 20

elif age >=12 and age < 60:
    print("ticket type: adult")
    price = 300
    if is_weekend:
        price = price + 50

else:
    print("ticket type: senior")
    price = 200
    if is_weekend:
        price = price + 20
print("Total price:", price)

# Loan approvel
salary = 60000
credit_score = 740
is_loan = True

if salary >= 30000:
    if credit_score >=700:
        if is_loan == False:
            print("your loan approve successfully:")
        else:
            print("Loan rejected: already have a loan")
    else:
        print("Loan rejected :Low credit score")
else:
    print(" Loan rejected: Low Salary")


######################## LOOPS #########################

# For Loop :  USED FOR ALREADY KNOWS HOW MANY TIME YOW WANT TO REPEAT

for i in range(5):   #stop at 5 0-4
    print(i)

for i in range(1,6):    #start and stop 1,6 0-5
    print(i)

for i in range(1,10,2): # start stop step 1,11,2. 1 3 5 7 9
    print(i)

for i in range (10,0,-2):   # start stop step reverse 10,0,-2. 10 8 6 4 2
    print(i)

for i in range(5): # for repeating something
    print("Pranav")

numbers = [10,20,30,40] #Using range() with list length

for i in range(len(numbers)):
    print("index:",i,"value:",numbers[i])


# Nested loop with range()
for i in range(3):
    for j in range(2):
        print("i=",i,"j=",j)

prizes = [100,200,300,400]

for prize in prizes:
    print(prize)

fruits = ["apple","banana","mango"]

for fruit in fruits:
    print(fruit)

######################### while Loop ##############
# Used when you don’t know how many times loop will run.

count = 1

while count <= 5:
    print(count)
    count +=1

num = 5
while num > 0:
    print(num)
    num -=1
print("done")

# while  True: #infinite loop  print continueslly
#     print("hureeee")


# Break
i = 1

while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1

# continue 

i = 0 

while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)


#   Check Positive, Negative, or Zero
number = float(input("Enter Number:"))

if number > 0 :
    print("positive number")
elif number < 0:
    print("Negative number")
else:
    print("zero")    

# Print Even Numbers from 1 to 20 (Using for loop)

for i in range(1,21):
    if i % 2 == 0:
        print(i)

# short method for even numbers
for i in range(2,21,2):
    if i % 2 == 0:
        print(i)

# Simple Login System (Using while loop)

correct_password = "admin1234"
passsword = ""

while passsword != correct_password:
    passsword = input("enter password:")
print("login successful")

# Table using loop
num = int(input("enter number:"))

for i in range(1,11):
    result = num * i
    print(num,"x",i,"=",result)

# for i in range(5):
#     print(i)

