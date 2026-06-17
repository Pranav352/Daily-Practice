p = [5,3,2,2,1,5,5,7,5,10]
r = [10,111,1,9,5,67,2]

for num in p:
    count = 0
    for x in r:
        if num == x:
            count += 1
    print(count)


print("\n")


n = [5,7,2,6,6,10,2,1,4,9]
m = [8,6,12,5,2,4,10,1,14,7]

has_list = [0] * 11

for num in n:
    has_list[num] += 1
    for num in m:
        if num < 1 or num > 10:
            print(0)
        else:
            print(has_list[num])

# Q-2
s= "a,c,b,u,y,c,c,a,a"
q =["a","d","y","u"]
hash_list = [0] * 26

for ch in s:
    asc_value = ord(ch)
    index = asc_value-97
    hash_list[index] += 1

    for ch in q:
        asc_value = ord(ch)
        index = asc_value - 97
    print(hash_list)


