           ############# Basic of decorators ################
def my_decorators(func):
    def wrapper():
        print("Somethon before function runs")
        func()
        print("somethin after function runs")
    return wrapper
def say_hello():
    print("Hello!")

say_hello = my_decorators(say_hello)
say_hello()

def decorators(de):
    def hello():
        print("something runs befor")
        de()
        print("something runs after")
    return hello
def say_hi():
    print("hey!")

say_hi = decorators(say_hi)
say_hi()

                 ########### @Decorators syntex #############

def my_decode(fun):
    def decode():
        print("Before")
        fun()
        print("After")
    return decode

@my_decode # its used for print main "my_decode" funcation
def hello():
        print("hey!")
hello()

def hi (fun):
    def hello():
        print("hello before")
        fun()
        print("hey after")
    return hello
@hi
def hey():
    print("How are you!")
hey()

################### Decorators with Arguments ###########

def hello(fun):
    def hey(hi):
        print("before")
        fun(hi)
        print("after")
    return hey
@hello
def hi(hi):
    print(f"hey!{hi}")
hi("ram")


def decode(fun):
    def my_decode(name):
        print("before")
        fun(name)
        print("after")
    return my_decode
@decode
def Dec(name):
    print(f"Hello:{name}")
Dec("ram")

        ########## Using *args and **kwargs (Best Practice) ########

def my_dewcorators(func):
    def wrapper(*args, **kwargs):
        print("before")
        result = func(*args, **kwargs)
        print("after")
        return result
    return wrapper

@my_dewcorators
def add():
    print("hello")
add()


import time
def my_time(fun):
    def timr(*args, **kwargs):
        start = time.time()
        fun(*args, **kwargs)
        end = time.time()
        print("Executation time:",end - start)
    return timr

@my_time
def slow_function():
    time.sleep(2)
slow_function()


def arg(fun):
    def my_arg(*args, **kwargs):
        print("before")
        result = fun(*args, **kwargs)
        print("after")
        return result
    return my_arg
@arg

def argument(name):
    print(f"Hello: {name}")
argument("preet")


        ##################### Class Method ###########
class circle:
    def __init__(self,radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius
    
    @classmethod
    def uni_circle(cls):
        return cls(1)
    







