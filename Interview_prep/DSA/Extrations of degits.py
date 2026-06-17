# Count of digits
# Reverse a number
# Check palindrome
# Armstrong Number


# Reverse a Number
n = 5873

num = n

while num > 0:
    last_digit = num % 10
    print(last_digit)
    num = num // 10

print("\n") # new line

# count of digits   
n = 5438
num = n                #SC = O(1) because we are using only one variable for counting the digits 
count = 0

while num > 0:
    count += 1
    num = num // 10          #TC = O(log10 (N))   which i used for devide for 10 so log 10
print(count)


print("\n") # new line

def count(n): #with function
    
    num = n
    count = 0

    while num > 0:
        count += 1
        num = num //10
    return count

print(count(7890))


from math import * # log10
def count(n): # with log10
    if n == 0:
        return 1
    else:
        return floor(log10(n)) + 1
print(count(7890))

# 
print("\n")
# 

# Check Palindrome

n =  12321  #palindrome         #SC = O(1) because we are using only one variable for reverse and num
# n= 1234 #not palindrome
num = n

reverse = 0

while num >0:
    last_digit = num % 10
    reverse = (reverse * 10) + last_digit
    num = num // 10         #TC = O(log10 (N)) because we are using log 10 for devide for 10

print(n == reverse)

if reverse == n:
        print("Palindrome")
else:
        print("Not Palindrome")

# 
print("\n")
# 


# Armstrong Number
n = 153 # armstrong
# n = 123 # not armstrong
num = n                         #SC = O(1) because we are using only one variable for total and num
total = 0
nod=len(str(n)) # number of digits

while num > 0:
     ld = num % 10
     total =total + (ld ** nod)
     num = num //10             #TC = O(log10 (N)) because we are using log 10 for devide for 10
print(total == n)

if total == n:
     print("Armstrog")
else:
     print("Not Armstrog")


# 
print("\n")
# 

     
# print factors / divisors
num = 20
result = []     #SC = O(K) where K is the number of factors of num 

for i in range(1,(num + 1)):        #TC = O(N) because we are iterating from 1 to num 
     if num % i == 0:
          result.append(i)      #TC = O(1) for appending an element to the list
print(result)



print("\n")


# Better Sollution
num = 10
result = []                      #n/2 and o(1) both are seperate and O(N/2) is for whole loop and O(1) is for checking if i is a factor of num and appending it to the list. so overall TC = O(N/2) which is better than O(N) in worst case when num is prime and we have to check all numbers from 1 to num/2
for i in range(1,num // 2):     #n/2 because no number can be a factor of num if it is greater than num/2 except num itself
     if num % i == 0:           #O(1) for checking if i is a factor of num.    
          result.append(i)      #O(N/2) in worst case when num is prime and we have to check all numbers from 1 to num/2
result.append(num)  # O(1) for appending num itself to the list of factors
print(result)




print("\n")



from math import sqrt
# optional solution

num = 36
result = []

for i in range(1,int(sqrt(num) +1)):                #TC = O(sqrt(N)) because we are iterating from 1 to sqrt(num) and for each i we are checking if it is a factor of num and if it is then we are appending both i and num//i to the list of factors. so overall TC = O(sqrt(N)) in worst case when num is a perfect square and we have to check all numbers from 1 to sqrt(num)
     if num % i == 0:
          result.append(i)
          if num // i != i:
               result.append(num // i)
print(result)   # if question about print only factors

# if question ask with sort()
result.sort()                   #TC = O(n log n) for sorting the list of factors
print(result)                   #SC = O(K)

# With sorting()full code  TC=O(sqrt(N) + O(N log N)) because we are iterating from 1 to sqrt(num) and for each i we are checking if it is a factor of num and if it is then we are appending both i and num//i to the list of factors. so overall TC = O(sqrt(N)) in worst case when num is a perfect square and we have to check all numbers from 1 to sqrt(num) and then we are sorting the list of factors which takes O(N log N) time. so overall TC = O(sqrt(N) + O(N log N)) which is better than O(N) in worst case when num is prime and we have to check all numbers from 1 to num/2   

print("\n")

# frequency of map // Dictionary
# Method - 1

nums = [5,6,7,7,1,9,111,1,1,5,1,1]
x = 1

freq_diq = dict() 
for i in range(0,len(nums)):
    if nums[i] in freq_diq:
         freq_diq[nums[i]] +=1          
    else:
        freq_diq[nums[i]] = 1
print(freq_diq)
print(freq_diq[x])

# Method - 2
nums = [5,6,7,7,1,9,111,1,1,5,1,1]
hash_map = {}
n = len(nums)
for i in range(0,n):
     hash_map[nums[i]] = hash_map.get(nums[i],0) + 1 
print(hash_map)




# want only unique characters with numbers:
#  i am pranav

p = "I am Pranav"

start = p.find("a")
end = p.rfind("a")

seen = " "
for i in range(start,end+1):
     if p[i] not in seen:
          seen += p[i]
print (seen)
