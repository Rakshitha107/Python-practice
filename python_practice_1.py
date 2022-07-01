# PYTHON INTRODUCTION

print("hello world!")

# NONE KEYWORD
def a_void_function():
  a = 1
  b = 2
  c = a+b

x = a_void_function()
print(x)

def improper_return_function (a):
    if( a % 2)==0:
      return True

x = improper_return_function(5)
print(x)

# BREAK KEYWORD
for i in range(1, 11):
    if i == 5:
        break
    print(i)

# if, else, elif example
def if_example(a):
    if a == 1:
        print ('one')
    elif a == 2:
        print ('two')
    else:
        print('something else')

if_example(2)
if_example(4)
if_example(1)

def double(num):
    """function to double the value"""
    return 2*num
    print(double.__doc__)

#assinging variables in python
website = "apple.com"
print(website)

a, b, c = 5, 4.5, "hello"

print(a)
print(b)
print(c)

x = y = z = "same"
print(x)
print(y)
print(z)

# literals
a = 0b1010 #binary literal
b = 100 #decimal literal
c = 0o310 #octal literal
d = 0x12c #hexadecimal literal

#float literal
float_1 = 10.5
float_2 = 1.5e2

#complex literal
x = 4.14j

print(a, b, c, d)
print(float_1, float_2)


#boolean literals
x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)

#use of special literals in python
drink = 'Available'
food = None

def menu(x):
    if x == drink:
        print(drink)
    else:
        print(food)

menu(drink)
menu(food)

#literals collection
fruits = ["apple", "banana", "grapes", "mango"]#list
numbers = (1, 2, 3)#tuple
alphabets = {'a':'apple', 'b':'ball'}#dictionary
vowels = {'a', 'e', 'i', 'o', 'u'}#set

print(fruits)
print(numbers)
print(alphabets)
print(vowels)

#python data types
a = 5
print(a, "is of type", type(a))#int

a = 2.0
print(a, "is of type", type(a))#float

a = 1+2j
print(a, "is complex number", isinstance(1+2j, complex))#complex

#list in python
a = [5, 10, 15, 20, 25, 30, 35, 40]

#a[2]=15
print("a[2] = ", a[2])

#a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])

#a[5:] = [30, 35, 40]
print("a[5:] = ", a[5:])

print("a[3:5] = ", a[3:5])

a = [1, 2, 3]
a[2] = 4
print(a)

#python strings
s = "this is a string"
print(s)
s = '''multiline
string'''
print(s)

s = 'Hello world!'

# s[4] = 'o'
print("s[4] = ", s[4])

# s[6:11] = 'world'
print("s[6:11] = ", s[6:11])

#python set
a = {5,4,3,2,1}
print("a =", a)
print(type(a))

#python dictionary
d = {1:'value', 'key':2}
print(type(d))
print("d[1] =", d[1])
print("d['key'] =", d['key'])

#implicit type conversion
num_int = 123
num_float = 1.23
print('datatype of num_int:', type(num_int))
print('dataype of num_float:', type(num_float))

print('value of num_int:', num_int)
print('value of num_float:', num_float)

#explicit type conversion
num_int = 123
num_str = "456"

print("Data type of num_int:",type(num_int))
print("Data type of num_str before Type Casting:",type(num_str))

num_str = int(num_str)
print("Data type of num_str after Type Casting:",type(num_str))

num_sum = num_int + num_str

print("Sum of num_int and num_str:",num_sum)
print("Data type of the sum:",type(num_sum))

#python input, output, import
print(1, 2, 3, 4, 5)
print(1, 2, 3, 4, 5, sep= '*')
print(1, 2, 3, 4, 5, sep='#', end='&')

#python import
import math
print(math.pi)

#python operators
x = 15
y = 4

# Output: x + y = 19
print('x + y =',x+y)

# Output: x - y = 11
print('x - y =',x-y)

# Output: x * y = 60
print('x * y =',x*y)

# Output: x / y = 3.75
print('x / y =',x/y)

# Output: x // y = 3
print('x // y =',x//y)

# Output: x ** y = 50625
print('x ** y =',x**y)

#comparison operator
x = 10
y = 12

# Output: x > y is False
print('x > y is',x>y)

# Output: x < y is True
print('x < y is',x<y)

# Output: x == y is False
print('x == y is',x==y)

# Output: x != y is True
print('x != y is',x!=y)

# Output: x >= y is False
print('x >= y is',x>=y)

# Output: x <= y is True
print('x <= y is',x<=y)

#logical operators
x = True
y = False

print('x and y is',x and y)
print('x or y is',x or y)
print('not x is',not x)

#identity operators
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

# Output: False
print(x1 is not y1)

# Output: True
print(x2 is y2)

# Output: False
print(x3 is y3)

#python namespace and scope
a = 2
print('id(2)=', id(2))
print('id(a)=', id(a))

a = 2
print('id(a) =', id(a))

a = a+1
print('id(a) =', id(a))

print('id(3) =', id(3))

b = 2
print('id(b) =', id(b))
print('id(2) =', id(2))

#example
def printhello():
    print("hello")
a = printhello
a()

#example 1
def outer_function ():
    a = 20
    def inner_function ():
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)
a = 10
outer_function()
print('a =', a)

#example 2
def outer_function ():
    global a
    a = 20
    def inner_function():
        global a
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)
a = 10
outer_function()
print('a =', a)
