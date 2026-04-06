######### List

# Ordered , Mutable (can change) , Allows duplicates

numbers = [1, 2, 3]
numbers.append(4)
numbers.sort()

numbers.remove(1)
numbers.pop(2)
print(numbers)


num = [5, 3, 6, 2, 1]
num.append(4)
num.remove(6)
num.sort()

print(num)


# append()

# remove()

# sort()

# pop()

########### Tuple

# Ordered

# Immutable (cannot change)
point = (10, 20)


########################### Dictionary

# Key-value pairs

# Mutable

# Keys must be unique

student = {"Name":"John","Age":24}
print(student["Name"])

# eys() , values() ,items() ,get()

######################################### Set

# Unordered , No duplicates ,Mutable

name = {1, 2, 3}
name.add(4)
print(name)
# Useful for:

# Removing duplicates

# Mathematical operations (union, intersection)

a = {1, 2, 3}
b = {3, 4, 5}

print(a & b)
print(a | b)