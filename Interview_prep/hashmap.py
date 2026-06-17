# hashMap
# Two Sum

def two_sum(nums, target):

    hasmap = {}

    for i, num in enumerate(nums):

        needed = target - num

        if needed in hasmap:
            return [hasmap[needed],i]
        hasmap[num] = i
print(two_sum([2,7,11,15],9))
print(two_sum([1,2,3],5))
print(two_sum([4,5,6],10)) 

# 2. Contains Duplicate
# Check if array contains duplicates.

def contains_dublicate(nums):

    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
print(contains_dublicate([1,2,3,4,2,1]))
print(contains_dublicate([12,14,22,24]))

