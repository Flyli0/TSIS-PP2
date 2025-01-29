import random

'''Task1 Converting grams'''
def ounce(a):
    ounces = 28.3495231 * a
    return ounces 

'''Task2 Converting temperature'''
def centigrade(b):
    C = (5 / 9) * (b - 32)
    print(C)

'''Task3 Puzzle'''
def solve(h = 35,l = 94):
    if l%2 == 0 and l-h >= h:
        rabbits = l / 4
        chickens = h - rabbits 
    else: 
        return 'No solution'
    print('num of rabbits = ', rabbits)
    print('num of chickens = ', chickens)

'''Task 4 Prime'''
def filter_prime(llist):
    i = 0
    while i < len(llist):
        count = 0
        if llist[i] != 1 and llist[i] != 2:
            for j in range(1,llist[i]+1):
                if llist[i]%j==0:
                    count += 1
                if count > 2:
                    llist.remove(llist[i])
                    i-=1
                    break
        i+=1

'''Task 5 Permutations'''
def permut(a):
    b = []
    for i in a:
        b.clear()
        b.append(i)
        for j in a:
            if j != i:
                b.append(j)
            for k in a:
                if k != i and k!= j :
                    b.append(k)
                    if len(b)==len(a):
                        print(''.join(b))
                        b.remove(k)
                        b.remove(j)
                    else:
                        b.remove(k)

'''Task 6 reverse'''
def rev(s):
    d = []
    d = list(s.split())
    d = reversed(d)
    s = ' '.join(d)
    print(s)

'''Task 7 (3,3)'''
def has_33(llist):
    count = 0
    sas = False
    for i in llist:
        if i == 3:
            count += 1
        else: 
            count = 0
        if count >= 2:
            sas = True
    print(sas)

'''Task 8 007'''

def James_bond(llist):
    sus = False
    a = ''.join(map(str,llist))
    if a.find('007') != -1:
        sus = True
    print(sus)

'''Task 9 Sphere value''' 
def calc_val(r):
    print((4.0/3.0)*3.14*(r**3))

'''Task 10 Unique'''
def uni(llist):
    a = set(llist)
    return a

'''Task 11 Palindrome'''
def pali(sstr = 'a'):
    if sstr == sstr[::-1]:
        print('Palindrome')
    else:
        print('Not palindrome')

'''Task 12 Histogram'''
def histo(llist):
    for i in llist:
        for j in range(i):
            print('*', end='')
        print()

'''Task 13 guess the num'''
def GtN():  
    A = random.randint(0, 20)
    print('Hello! What is your name?')
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    print("To exit the game enter : exit")
    b = 0
    while int(b) != A:
        b = input()
        if b != "exit":
            if int(b) > A:
                print("Too high")
            elif A > int(b):
                print("Too low")
        else: break
    if int(b) == A:print("You guessed it right! CONGRATULATIONS!!!!!!")



       