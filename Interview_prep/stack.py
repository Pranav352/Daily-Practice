
s = []

s.append("https://edition.cnn.com/")
s.append("https://edition.cnn.com/world")
s.append("https://edition.cnn.com/world/india")
s.append("https://edition.cnn.com/world/americas")


# Write a function in python that can reverse a string using stack data structure. Use Stack class from the tutorial.
# reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"

def reverse_string(s):
    stack = []
    for char in s:
        stack.append(char)
    rstr = ""
    while stack:
        rstr += stack.pop()
    return rstr

if __name__ == "__main__":
    print(reverse_string("We will conquere COVID-19"))