

# Functions - Functions are used to seperate functionalities in a program.
'''
Functions are of two types:

Inbuilt functions - print(), input(), append(), insert(), values(), items()
User Defined functions - our examples

Functions are executed only when called

syntax :

def functionname():

    s1
    s2
    s3

'''


'''
# Without function
name = input("Enter your name : ")
age = int(input("Enter your age : "))
print("Name is ",name)
print("Age is ",age)

'''


'''
#Using a function

print("Before")
def user_inputs():

    name = input("Enter your name : ")
    age = int(input("Enter your age : "))
    print("Name is ",name)
    print("Age is ",age)

user_inputs()
print("After")
'''


'''
#Using a function - Parameterised function (Passing values to a function)

print("Before")
def user_inputs(name, age):

    print("Name is ",name)
    print("Age is ",age)

name = input("Enter your name : ")
age = int(input("Enter your age : "))
user_inputs(name, age)
print("After")
'''

'''
# Using Functions - Parameterised (Returning values from a function)
def user_input():
    name = input("Enter your name : ")
    age = int(input("Enter your age : "))
    return name, age

name, age = user_input()
print("Name is ",name)
print("Age is ",age)
'''


'''
# Function - Passing values to a function and changing valraible names
print("Before")
def user_inputs(n, a):

    print("Name is ",n)
    print("Age is ",a)

name = input("Enter your name : ")
age = int(input("Enter your age : "))
user_inputs(name, age)
print("After")
'''


# Functions - Returning values from a functions and changing variable names
def user_input():
    name = input("Enter your name : ")
    age = int(input("Enter your age : "))
    return name, age

n, a = user_input()
print("Name is ",n)
print("Age is ",a)


print("1) Add\n2) Sub\n3) Mul\n4) Div")
choice = int(input("Pleas"))
