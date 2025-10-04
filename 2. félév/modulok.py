import random
import math
from functools import cache
from sys import getrecursionlimit, setrecursionlimit

def modulok_bevezeto():
    print(getrecursionlimit()) # 1000
    setrecursionlimit(5000)
    print(getrecursionlimit()) # 5000
    
    random.seed("almafa")
    print(random.randrange(1, 11)) # random szám 1-10 között
    print(random.randint(1,2))     # random szám 1-2 között
    print(random.randrange(0, 101, 5))  # random szám 1-100 között, 5 ösével
    
    print(math.pi) # 3.141592653589793
    print(math.e)
    print(math.tau) # 2 * pi
    print(math.inf) # végtelen, minden számtól nagyobb
    print(math.inf > 629847632985482365782) # True
    print(-math.inf < 1000)
    print(math.ceil(4.0000001)) # ceiling (plafon), felfelé kerekít
    print(math.floor(4.0000001)) # padló, lefelé kerekít
    print(math.factorial(6)) #720
    print(math.acos(1))

@cache
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)
