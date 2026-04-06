
# sentence = input("enter sentence:")

# word = ""
# reversed_sentence = ""

# for ch in sentence:
#     if ch != " ":
#         word = word + ch
#     else:
#         reversed_sentence = word + " " + reversed_sentence
#         word = ""
# reversed_sentence = word + " " + reversed_sentence

# print("reversed sentence:",reversed_sentence)



# def find_missingnum(num):
#     n = len(num) + 1
#     expsum = n*(n + 1) // 2
#     actual = sum(num)

#     return expsum - actual

# num = [1,2,4,5]
# miss_sum = find_missingnum(num)
# print("Missing Num:",miss_sum)


string = input("Enter sentence: ")

for char in string:
    if string.count(char) == 1:
        print("found",char)
        break
else:
        print("not found")






