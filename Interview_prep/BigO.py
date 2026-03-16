# O(n) Time complexity

def get_numbers(numbers):
    num = []
    for n in numbers:
        num.append(n * n)
    return num
numbers = [2,5,8,9]
get_numbers(numbers)

# O(1)
def find_pe(price,pen,index):
    pe=price[index]/pen[index]
    return pe

# O(n2)
# find dublicate from list

number = [10 , 15 , 20 , 10 , 40 , 15]

for i in range(len(number)):
    for j in range(i + 1 , len(number)):
        if number[i] == number[j]:
            print(number[i],"is dublicate")
            break

# same but with n2 an n iterations

nu = [4 , 8 , 12 , 4 , 12 , 16]
dublicate = []

for i in range(len(nu)):
    for j in range (i + 1 , len(nu)):      #n2
        if nu[i] == nu[j]:
            dublicate = nu[i]
            break
for i in range(len(nu)):                #n
    if nu [i] == dublicate:
        print(i)
