# Azokat a függvényeket amik önmagukat hívják meg, rekurzív függvényeknek hívjuk
# 2 dologra mindig figyeljünk:
#   Legyen egy olyan pont, amikor a függvény már nem hívja meg önmagát
#   Ezt a pontot érhesse is el mindenképp a függvény

def rekurzio(n: int):
    if n <= 0:
        return
    print("Szia!")
    rekurzio(n-1)

rekurzio(3)

# Faktoriális
# 4! = 4 * 3 * 2 * 1 = 24
# 4! = 4 * 6 = 24
# 3! = 3 * 2 = 6
# 2! = 2 * 1 = 2
# 1! = 1
# 0! = 1
# n! = n * (n-1)!       (ahol n egy pozitív egész szám)

def fakt(n: int) -> int:
    if n == 1 or n == 0:
        return 1
    return n * fakt(n-1)

print(fakt(6))
print(fakt(10))

# Rekurzív sorozatok:
# a(n) = 3 + a(n-1)
# a(1) = -20
# -20, -17, -14, -11, -8, ...

def a(n: int) -> int:
    if n == 1:
        return -20
    return 3 + a(n-1)

print([a(i) for i in range(1, 11)])

# b(n) = 1.1 * b(n-1) + 2
# b(1) = 10

def b(n:int) -> float:
    if n == 1:
        return 10
    return 1.1 * b(n-1) + 2

print([b(i) for i in range(1, 11)])

# c(n) = c(n-1) + 2 * c(n-2) + 2
# c(1) = -2
# c(2) = 5

def c(n:int) -> int:
    if n == 1:
        return -2
    if n == 2:
        return 5
    return c(n-1) + 2 * c(n-2) + 2

print([c(i) for i in range(1, 17)])

# d(n) = 9 + d(n-1)
# d(1) = -3

def d(n:int)->int:
    if n == 1:
        return -3
    return 9 + d(n-1)

# e(n) = e(n-1)^2
# e(1) = -2

def e(n:int)->int:
    if n == 1:
        return -2
    return e(n-1)**2


print([d(i) for i in range(1, 11)])
print([e(i) for i in range(1, 8)])

# fib(n) = fib(n-1) + fib(n-2)
# fib(1) = fib(2) = 1
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

from functools import cache

@cache
def fib(n:int)-> int:
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

i = 1
while True:
    print(f"fib({i}) digit count = {len(str(fib(i)))}")
    if i > 20:
        break
    i += 1

call_counter = 0

def double_recursion(n: int):
    global call_counter
    call_counter += 1
    if n == 0:
        return
    double_recursion(n-1)
    double_recursion(n-1)

@cache
def double_recursion_cached(n: int):
    global call_counter
    call_counter += 1
    if n == 0:
        return 1
    double_recursion_cached(n-1)
    double_recursion_cached(n-1)

double_recursion(25)
print(f"A double_recursion függvény {call_counter} függvényhívást hajtott végre...")

call_counter = 0
double_recursion_cached(25)
print(f"A double_recursion_cached függvény {call_counter} függvényhívást hajtott végre...")