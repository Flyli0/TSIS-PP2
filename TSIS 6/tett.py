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
