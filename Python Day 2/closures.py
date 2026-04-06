                     ################ Closures ###############

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function
closuar_function = outer_function(10)
print(closuar_function(5))






def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter
counter = make_counter()
print(counter())
print(counter())

