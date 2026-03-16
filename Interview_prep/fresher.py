# # arrays

# arr = [1 , 2 , "Pranav" , 3.14 , True]
#      # 0 ,  1 ,    2 ,      3 ,  4.   indixing

# print(arr[1])

# arr[2] = 3
# print(arr)

# arr[4] = 4
# print(arr)


# arr = [1,2,3,4]

# value = int(input("Enter value:"))

# arr.append(value)
# print(arr)



# arr = [1,2,3,4,5]

# arr.insert(5,6)#index 5 , value 6
# print(arr)



# arr = [1,2,3,4]

# arr.remove(2) #removes the number 2 from the array

# arr.pop() #removes the last element from the array

# print(arr)



# arr = [1,2,3,4,5]

# print(arr[1:4]) # slicing 
# print(arr[-2:])# slicing negative indexing 



# arr = [ 1,2,3,4,5]

# if 2 in arr:
#     print(" is present in the array")
# else:
#     print(" is not present in the array")


# arr = [1,2,3,4,5,-2]

# print(min(arr))
# print(max(arr))
# print(sum(arr))
# print(len(arr))

# arr.sort()
# print(arr)

nums = [1,2,3,4,5,6,7]
k = 3

def rotate(nums, k: int) -> None:
    n = len(nums)
    for _ in range(k):
        last = nums[-1]
        for i in range(n-1,0,-1):
            # print(nums)
            nums[i] = nums[i-1]
        print(nums)
        nums[0] = last
    return nums
print(rotate(nums, k))



# find dublicate elements
# with using set

def find_dublicate(arr):
    seen = set()
    dublicate = set()

    for num in arr:
        if num  in seen:
            dublicate.add(num)
        else:
            seen.add(num)
    return list(dublicate)
arr = [1,2,3,4,2,3,5]
print(find_dublicate(arr))


def dublicate(arr):
    seen = set()
    dublicate = set()

    for num in arr:
        if num in seen:
            dublicate.add(num)
        else:
            seen.add(num)
        return list(dublicate)
arr = [1,2,3,4,2,3,5,6]
print(dublicate(arr))

# find missing number
# n*n+1//2 sum of arr
def find_missing_number(arr,n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)

    return expected_sum - actual_sum
arr = [1,2,4,5,6]
print(find_missing_number(arr, 6))


def miss_num(arr,n):
    expected = n *(n+1) //2
    actual = sum(arr)

    return expected - actual
arr = [1,2,4,5,6,7]
print(miss_num(arr,7))



# rotate array

def rotate_array(arr,k):
    k = k % len(arr)
    return arr[-k:] + arr[:-k]
arr = [1,2,3,4,5,6]
print(rotate_array(arr,2))

# maximum subarray (kadane's algorithm)
# find the subarray with the largest sum
# [-2,1,-3,4,-1,2,1,-5,4]

def max_subarray(arr):
    max_sum = arr[0]
    current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(num,current_sum + num)
        max_sum = max(max_sum,current_sum)
        
    return max_sum
arr = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray(arr))


                ####### array Data Stracture ######
# EX-1

# exp = [2200, 2350 ,2600, 2130, 2190]

# 	1. January -  2200
#  	2. February - 2350
#     3. March - 2600
#     4. April - 2130
#     5. May - 2190

# Create a list to store these monthly expenses and using that find out,
#
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this information.

exp = [2200, 2350 ,2600, 2130, 2190]

print("1. in february,you spent extra",exp[1] - exp[0],"dollers compare to january")

print("2.total expense in first quarter is",exp[0] + exp[1] + exp[2],"dollers")

print("3. you spent exactly 2000 dollars in any month?", 2000 in exp)

exp.append(1980)
print("4.  expanse at end of june ", exp)

exp[3] = exp[3] - 200
print("expense after return 200 dollar in april",exp)


# EX-2

# hero=['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

hero =['spider man','thor','hulk','iron man','captain america']

print("1.length of hero is:",len(hero))
hero.append('black panther')
print("2.add black panther:",hero)

hero.remove('black panther')
hero.insert(3,'black panther')
print("3.add black panther after hulk:",hero)

hero[1:3] = ['doctor strange']
print("4. replace thor and hulk with doctor strange:",hero)

hero.sort()
print("5.sort heros in alphabetical order:",hero)

# EX-3 
# Create a list of all odd numbers between 1 and a max number. 
# Max number is something you need to take from a user using input() function  

max_num = int(input("Enter max number:"))

odd_num = []

for i in range(1,max_num):
    if i % 2 == 1:
        odd_num.append(i)
    print("odd numbers:",odd_num)


class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beggining(self,data):
        node = Node(data,self.head)
        self.head = node
        



    
    









