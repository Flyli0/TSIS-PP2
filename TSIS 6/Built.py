'''''''''''''''''''''''''''Task 1'''''''''''''''''''''''''''
import math
import functools as ft
import operator as op
ft.reduce(op.mul([1, 2, 3, 4, 5, 6]))

'''''''''''''''''''''''''''Task 2'''''''''''''''''''''''''''
import operator as op
import math
import functools as ft
def low(x):
    if x.islower() == True:
        s = 1
        return int(1)
    else:
        return 0
b = str(input())
countu = 0
countl = 0
a = list(map(low,b))
print(a)
countu = ft.reduce(op.add,(list(map(low,b))))
print(countu,len(b)-countu)

'''''''''''''''''''''''''''Task 3'''''''''''''''''''''''''''
s = str(input())
k = ''.join(reversed(s))
if s == k:
    print('Yes')
else:
    print('No')

'''''''''''''''''''''''''''Task 4'''''''''''''''''''''''''''
import time
a = int(input())
d = int(input())
time.sleep(d/1000)
print(math.sqrt(a))

'''''''''''''''''''''''''''Task 5'''''''''''''''''''''''''''
da = (True,False,True,True)
print(all(da))