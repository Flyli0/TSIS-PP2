import math

'''''''''''''Task 1'''''''''''''
class MyStr:
    def __init__(self,content):
        self.cont = content
    
    def getString(self,string):
        self.cont = string

    def printString(self):
        print(self.cont.upper())

a = MyStr('a')
#a.getString(str(input()))
a.printString()

'''''''''''''Task 2'''''''''''''
class Shape:
    def __init__(self):
        self.arr = 0
    def area(self):
        print(self.arr)

class Square(Shape):
    def __init__(self,length):
        self.length = length
        self.arr = self.length**2
x = Square(2)
x.area()

'''''''''''''Task 3'''''''''''''

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def compArea(self):
        self.arr = self.length*self.width

'''''''''''''Task 4'''''''''''''
class Point:
    def __init__(self,x,y,):
        self.x = x
        self.y = y
    def show(self):
        print('x coordinate: ',self.x)
        print('y coordinate: ',self.y)
    def move(self,xx,yy):
        self.x = xx
        self.y = yy
    def dist(self,point):
        print('distance: ',math.sqrt((self.x - point.x)**2+(self.y-point.y)**2))

p1 = Point(2,3)
p2 = Point(4,5)
p1.dist(p2)

'''''''''''''Task 5'''''''''''''
class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance 
    def deposit(self,val):
        self.balance += val
    def withdraw(self,money):
        if self.balance >= money:
            self.balance -= money
            print(f'You successfuly withdrew: {money}t ')
        else:
            print('Your balance is too low')

ac1 = Account('Me',100000)
ac1.withdraw(9123)
ac1.withdraw(120000)

'''''''''''''Task 5'''''''''''''
nums = [1,2,3,4,5,6,7,8,9,52]
res = list(filter(lambda x: lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1)) ,nums))