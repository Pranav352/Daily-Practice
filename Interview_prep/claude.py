#1. string problem. #Time Complexity: O(n) # Space Complexity: O(n)
# Problem: Write a program to reverse a string without using string slicing.


# Solution 1 - Using loop:
def reverse_string(s):
    reversed_str = ""

    for char in s:
        reversed_str = char + reversed_str
    return reversed_str
# example
# input_string = "Hello"
# reverse_string = reverse_string(input_string)
# print("original string:", input_string)
# print("reversed string:", reverse_string)

print(reverse_string("Hello")) #output:"olleh"

# Solution 2 - Using slicing
def reverse_string(r):
    return r[::-1]
print(reverse_string("Hey")) #output: yeh



# Solution 3 - Using recursion:
def rev_str(p):
    if len(p) == 0:
        return p
    else:
        return rev_str(p[1:]) + p[0]
print(rev_str("python")) #output: nohtyp


# 2. Problem: Check if a string is a palindrome (reads same forwards and backwards).
# Time Complexity: O(n).    # Space Complexity: O(1) for two-pointer, O(n) for slicing
# Solution 1 - Two pointer approach:

def is_palindrome(p):
    left, right = 0, len(p) - 1

    while left < right:
        if p[left] != p[right]:
            return False
        left +=1
        right -=1
    return True
print(is_palindrome("MadaM")) # Output: True
print(is_palindrome("hey")) # Output: false

# Solution 2 - Using string slicing:

def iss_palindrome(i):
    return i == i[::-1]
print(iss_palindrome("HaaH")) #Output: True
print(iss_palindrome("hello")) #Output: False


# 3. Count Vowels and Consonants
# Time Complexity: O(n). # Space Complexity: O(1)

def count_volves_consonants(c):

    volves = "aeiouAEIOU"
    volve_count = 0
    consonants = 0

    for char in c:
        if char in volves:
            volve_count += 1
        elif char.isalpha():
            consonants +=1
    return volve_count, consonants
print(count_volves_consonants("Hello World")) #Output: (3, 7)
print(count_volves_consonants("hello")) #Output:(2,3)

# 4. Remove Duplicates from String
# Time Complexity: O(n). # Space Complexity: O(n)













