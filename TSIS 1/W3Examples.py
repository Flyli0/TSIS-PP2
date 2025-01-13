import math 

print("Hello world") 

#this is a comment 
'''multiline comment'''

s = int(input())
if s > 2:
    print("Hello world")

x = 5
y = "John"
print(x)
print(y)

'''Allowed variable names'''
myvar = "John"
my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

x, y, z = "Orange", "Banana", "Cherry"
# Output of vars
print(x, y, z)
x = "Python"
y = "is"
z = "awesome" #this is global vars
def myfunc():
  l = 1 #This is local variable
  print("Python is " + l)

x = 5
print(type(x)) #type definig exmpl

'''Numbers'''
x = 1    # int
y = 2.8  # float
z = 1j   # complex

'''Casting'''
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

'''Strings'''
print("Hello")
print('Hello')

b = "Hello, World!"
print(b[2:5]) #Slicing

a = "Hello, World!"
print(a.upper()) #Modifying by method .upper

a = "Hello"
b = "World"
c = a + b
print(c) #Concatenation

age = 36
txt = f"My name is John, I am {age}" #formatting strings
print(txt)

txt = "We are the so-called \"Vikings\" from the north." #escape char \

