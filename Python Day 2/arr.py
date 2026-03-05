


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
