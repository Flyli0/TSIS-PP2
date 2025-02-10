'''Task1 '''
def mygen(x):
    a = 1
    while a < x:
        yield 2**a 
        a+=1
for i in mygen(4):
  print(i)

'''Task2 '''
n = int(input())
print('Eveens')
s = (i for i in range(n+1) if i%2 == 0)
for i in s:
   print(i)

'''Task3 '''
def mygen2(x):
    a = 1
    while a < x:
        if a%3 == 0 or a%4 == 0:
           yield a 
        a+=1
print('Omagaaaaaad')
for i in mygen2(15):
    print(i)

'''Task4 '''
print('squarres')
def square(x,y):
    a = x
    while a <= y:
           yield a**2
           a+=1

for i in square(2,11):
    print(i)

'''Task5 '''
print('taaaaaaaaaaask 5')
def mygen3(x):
    a = x
    while a >= 0:
        yield a
        a-=1
for i in mygen3(16):
  print(i)
