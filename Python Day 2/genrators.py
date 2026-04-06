
           ################## Genrators ###################
# using yield

def my_genrator():
    for i in range (5):
        yield i #it repeat one at a time
gen = my_genrator()
print(next(gen))
print(next(gen))
print(list(gen))



# Using genrator expression

gen_exp = (x**2 for x in range(5))
print(next(gen_exp))
print(list(gen_exp))