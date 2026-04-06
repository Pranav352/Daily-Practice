# Write a program to reverse a string

text = "Python"

reverse = text[::-1]
print(reverse)

# write a program to check whethere the number is even or odd

num = 10

if num % 2 == 0:
    print("even")
else:
    print("odd")


# find the largest number in list

number = [10, 50, 100, 200, 40]

largest = max(number)

print(largest)

# without built in function

numbers = [20, 1100, 1244, 44,]

larger = numbers[0]

for i in numbers:
    if i > larger:
        larger = i

print(larger)

# count vowels in string

texts = "Hello Python"

vowels = "aeiou"
count = 0

for char in texts:
    if char in vowels:
        count += 1
print(count)


# check whether a string is a palindrome 

mam = "madam"

if mam == mam[::-1]:
    print("IS Palindrome")
else:
    print("Note Palindrome")

# write a program to find factorial of the number

n = 5
factorial = 1

for i in range(1, n+1):
    factorial *= i
print(factorial)

# print fibonaci series

abc = 10

a, b = 0,1

for i in range(abc):
    print(a)
    a, b = b, a+b

# Remove dublicate from list

dub = [1,2,3,4,2,4]

unique = list(set(dub))

print(unique)

# swap two variable without using thired variable
a=10
b=20

a,b = b,a
print("a:",a,"b:",b)

# check if a number is prime or not
nu = 7

for i in range(2,nu):
    if nu % i ==0:
        print("Not Prime")
        break
else:
        print("Is Prime")

# count character frequency in string

string = "hello"

frequency = {}

for char in string:
    frequency[char] =frequency.get(char,0)+1

print(frequency)

# find second largest number in list

lis = [100,400,600,200400]
lis.sort()
print(lis[-2])

# merge two dictionaries

a1={"a":1,"b":2}
b2={"c":3,"d":4}

merge = {**a1,**b2}
print(merge)

# sum of element in list

ele = [1,2,3,4]

print(sum(ele))


# find missing number in list
i = [1,2,3,4,5,6,8]

n = 8

missing_num = n*(n+1)//2 - sum(i)

print(missing_num)













