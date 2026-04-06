# a function is a reusable block of code

def greet(name):
    return("Hello",name)
print(greet("Alice"))


square = lambda x: x * x
print(square(5))

# scope in python

x = 10 # Global

def test():
    x = 5 # Local
    print(x)
test()
print(x)

x = 10

def change():
    global x
    x = 20
change()
print(x)



