# PYTHON FUNCTIONS

# example of a function
from pyrsistent import b


def greet(name):
    """
    This functions greets to
    the person passed in as
    a parameter
    """
    print("Hello, " + name + ". Good morning!")

greet('paul')

# example of return
def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""

    if num >= 0:
        return num
    else:
        return -num


print(absolute_value(2))

print(absolute_value(-4))

# example to illustrate scope of a variable inside a function
def my_func():
    x = 10
    print("Value inside function:",x)

x = 20
my_func()
print("Value outside function:",x)

# python function arguments
#user defined functions
def greet(name, msg):
    """this function grrets to the person with the provided message"""
    print("Hello", name + ',' + msg)

greet("Monica", "Good morning!")

# python arbitary arguments
def greet(*names):
    """this function greets all the person in the names tuple."""
    for name in names:
        print("Hello", name)

greet("Monica", "Luke", "steve", "kim")

# python recursion
#example of a recursive function
def factorial(x):
    """this function is to find factorial of an integer"""
    if x == 1:
        return 1
    else:
        return(x * factorial(x-1))

num = 3
print("The factorial of", num, "is", factorial(num))

#python anonymous/lambda function
double = lambda x:x*2
print(double(5))

#exaple instead of lambda
def double(x):
    return x*2
    print(double(5))

#program to filter out only the even items from a list
my_list = [1, 5 ,4, 7, 5, 7]
new_list = list(filter(lambda x: (x%2 == 0), my_list))
print(new_list)

#python global, local ad nonlocal variables
#global varibles
x = "global"
def foo():
    print("x inside:", x)

foo()
print("x outside:", x)

#local variables
def foo():
    y = "local"
    print(y)

foo()

#global and local varibles
x = "global"

def foo():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)

foo()

#global variable and local variable with same name
x = 5
def foo():
    x = 10
    print("local:", x)

foo()
print("global:", x)

#nonlocal variables
def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()

#python global keyword
c = 1
def add():
    print(c)
add()

#modifying variables from inside which gives error
c = 1
def add():
    #c = c+2
    print(c)
add()

#modifying variables from inside using global
c = 0 # global variable

def add():
    global c
    c = c + 2 # increment by 2
    print("Inside add():", c)

add()
print("In main:", c)

#global nested function
def foo():
    x = 20

    def bar():
        global x
        x = 25
    
    print("Before calling bar: ", x)
    print("Calling bar now")
    bar()
    print("After calling bar: ", x)

foo()
print("x in main: ", x)

#python modules
def add(a, b):
        result = a + b
        return result