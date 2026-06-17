# length of list. Big - oh O(1)
lst = [12,14,15,16,20,21]
w = len(lst)
print(w)


# set average case o(1) worst case o(n)
set = {5,2,6,4,1}
if 1 in set:
    print ("found")
else:
    print ("Not found")


# dictionary average case o(1) worst case o(n)
# key       value
# 'a'       1
# 'b'       2
# 'c'       3

dict = {'a':1, 'b':2, 'c':3}
if 'b' in dict:
    print("Yes")
else:
    print("No")