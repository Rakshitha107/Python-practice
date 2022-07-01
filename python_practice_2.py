# PYTHON FLOW CONTROL

#python if statement
import numbers


num = 3
if num > 0:
    print(num, "is a positive number")
print("this is always printed")

num = -1
if num > 0:
    print(num, "is a positive number")
print("this ia also always printed")

#python if else statement
num = 3
if num >= 0:
    print("positive or zero")
else:
    print("negative number")

#python if elif else statement
num = 3.5
if num > 0:
    print("positive number")
elif num == 0:
    print("zero")
else:
    print("negative number")

#python nested if statement
num = float(input("Enter a number:"))
if num >= 0:
    if num == 0:
        print("zero")
    else:
        print("positive number")
else:
    print("negative number")
             
#example
num = int(input("enter a number:"))
if num >= 0:
    print("positive")
else:
    print("negative")

#python for loop
#program to find sum of all numbers stored in list
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 114]
sum = 0
for val in numbers:
    sum = sum + val
    print("The sum is", sum)

#example   
num = [5, 4, 6, 8]
sum = 1
for val in num:
    sum = sum + val
    print("the sum is", sum)

print(range(10))
print(list(range(10)))
print(list(range(2, 8)))
print(list(range(2, 20, 3)))

#program to iterate through a list using indexing
genere = ['pop', 'rock', 'jazz']
for i in range(len(genere)):
    print("i like", genere[i])

#for loop with else
digits = [0, 1, 5]
for i in digits:
    print(i)
else:
    print("No items left")

#program to display students marks from record
student_name = 'raju'
marks = {'james': 90, 'jules': 67, 'jacky': 39}

for student in marks:
    if student == student_name:
        print(marks[student])
        break
    else:
        print("No entry with that name found")

#python while loop
n = int(input("Enter n :"))
sum = 0
i = 1
while i <= n:
    sum = sum + i 
    i = i+1
    print("the sum is:", sum)

#Example to illustrate the use of else statement with the while loop
counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")

#Python break and continue
#use of break staement inside the loop
for val in "string":
    if val == "i":
        break
    print(val)
print("the end")

#use of continue statement inside the loop
for val in "string":
    if val == "i":
        continue
    print(val)
print("the end")

#python pass statement
'''pass is just a placeholder for 
functionally to be added later.'''
sequence = {'p', 'a', 's', 's'}
for val in sequence:
    pass
    