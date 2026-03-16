


arr = [1,3,4,2,2]



for i in range(len(arr)):    
    for j in range(i + 1, len(arr)):  
        if arr[i] == arr[j]:
            print(arr[j])


# def find_dublicate(arr):
   

#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[i] == arr[j]:
#                 print(arr[j])
#     return find_dublicate

# arr = [1,3,4,2,2]
# print(find_dublicate(arr))

def find_deblicate(arr):
    arr.sort()

    dublucate = []

    for i in range (len(arr)):
        if arr[i] == arr[i - 1]:
            dublucate.append(arr[i])
    return dublucate

arr = [1,3,4,2,2]
print("dublicates are;", find_deblicate(arr))



# Pivot index of array interview question in aimdek 

class solution:
    def pivotIndex(self,nums: list[int]) -> int:
        totalsum = sum(nums) #o(n)2
        leftsum = 0

        for i in range(len(nums)):
            rightsum= totalsum - leftsum - nums[i]

            if leftsum == rightsum:
                return i
            leftsum += nums[i]
        return -1


    
# product of array except self
class Solution:
    def productexcept(self,nums: list[int])->int:
        result = [1] * (len(nums))

        prefix = 1
        for i in range (len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        return result



