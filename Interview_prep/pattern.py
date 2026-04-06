# *
# **
# ***
# ****
# *****

for i in range(1,6):
    print("*"*i)

print("\n")


# *****
# ****
# ***
# **
# *

for i in range(5,0,-1):
    print("*"*i)

print("\n")

# 1
# 12
# 123
# 1234
# 12345

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()
print("\n")    

# 1
# 22
# 333
# 4444
# 55555

for i in range(1,6):
    print(str(i)*i)

print("\n")

#     *
#    ***
#   *****
#  *******
# *********

for i in range(1,6):
    print(" "*(5-i) +"*" *(2*i-1))

print("\n")

# *********
#  *******
#   *****
#    ***
#     *

for i in range(5,0,-1):
    print(" "*(5-i)+"*" *(2*i-1))

print("\n")

# *****
# *****
# *****
# *****
# *****

for i in range (5):
    print("*"*5)
print("\n")

# *****
# *   *
# *   *
# *   *
# *****

for i in range(5):
    if i==0 or i==4:
        print("*"*5)
    else:
        print("*" + " "*3+ "*")
print("\n")

# 1
# 2 3
# 4 5 6
# 7 8 9 10

num = 1
for i in range(1,5):
    for j in range(i):
        print(num,end=" ")
        num +=1
    print()
print("\n")

# 1
# 121
# 12321
# 1234321

for i in range(1,5):
    for j in range(1,i+1):
        print(j,end="")
    for j in range(i-1,0,-1):
        print(j,end="")
    print()





   

