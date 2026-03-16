# 1. Find the largest element in a list
# 👉 Example: [3, 5, 2, 9, 1] → 9

def largest_number(arr):
    if not arr:
        return None  # Handle empty list case
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num
arr = [3, 5, 2, 9, 1]
print(largest_number(arr))  # Output: 9


# 2.
# find smallest element in list
# 👉 Example: [3, 5, 2, 9, 1] → 1

def small_number(arr):
    if not arr:
        return  None  # Handle empty list case
    min_num = arr[0]
    for num in arr:
        if num <min_num:
            min_num = num
    return min_num
arr = [3, 5, 2, 9, 1]
print(small_number(arr))  # Output: 1

# 3. Reverse a list
# 👉 Without using built-in functions (important for interviews)

def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr)-1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr
arr = [1, 2, 3, 4, 5]
print(reverse_list(arr))  # Output: [5, 4, 3, 2, 1]

# 4. Count occurrences of an element
# 👉 Example: count how many times 2 appears in [1,2,3,2,4,2]

def count_occurrences(arr, target):
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count
arr = [1, 2, 3, 2, 4, 2]
print(count_occurrences(arr,2))  # Output: 3

# 5. Sum of all elements in a list

def sum_of_list(arr):
    total = 0
    for num in arr:
        total += num
    return total
arr = [1, 2, 3, 4, 5]
print(sum_of_list(arr))  # Output: 15

# 6. Check if element exists in list
# 👉 Return True/False

def element_exists(arr, target):
    for num in arr:
        if num == target:
            return True
    return False

arr = [1, 2, 3, 4, 5]
print(element_exists(arr,3))  # Output: True
print(element_exists(arr,6))  # Output: False




    