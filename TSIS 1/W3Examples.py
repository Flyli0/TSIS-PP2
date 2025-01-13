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