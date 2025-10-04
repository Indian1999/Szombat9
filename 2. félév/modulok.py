import random
import math
from functools import cache
from sys import getrecursionlimit, setrecursionlimit
import numpy as np              # terminálba: pip install numpy
import matplotlib.pyplot as plt # pip install matplotlib
from matplotlib.colors import LinearSegmentedColormap

image = [
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,1,1,0,0,1,1,0],
    [0,1,1,0,0,1,1,0],
    [0,0,0,1,1,0,0,0],
    [0,0,1,1,1,1,0,0],
    [0,0,1,1,1,1,0,0],
    [0,0,1,0,0,1,0,0]
]

paletta = LinearSegmentedColormap.from_list("creeper", ["green", "black"])
plt.imshow(image, cmap = paletta)
plt.axis("off")
plt.savefig("creeper.png")
plt.show()

def numpy_bevezeto():
    tomb = np.array([7,3,6,3,2])
    print(tomb)
    print(type(tomb)) # <class 'numpy.ndarray'>
    tomb = np.zeros(10)
    print(tomb) # [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
    mtx = np.zeros((5, 8))
    print(mtx)
    tomb[0] = 5
    print(tomb)
    tomb = tomb.reshape(2, -1) # Fontos: 2*5 = 10 = len(tomb)
    print(tomb)
    szamok = np.random.randint(1, 11, size = (6, 4)) # 1-10 között random értékek
    print(szamok)
    print(szamok.sum())
    print(szamok.max())
    print(szamok.mean()) # Átlag
    print(szamok.std())  # Standard Deviation (szórás)
    print(szamok.shape)  # (6, 4)

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
