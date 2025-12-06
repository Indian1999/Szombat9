lista = [4,6,3,2,1,1,5,6]

#immutable objektum (nem módosítható)
myTuple = (4, 1, 5, 6, 3, 2, 6, 4)
print(myTuple)
print(type(myTuple))


# NEM LEHET:
def tiltott():
    myTuple.append()
    myTuple[4] = 8
    del myTuple[2]

myTuple.count(3) # 1
myTuple.index(6) # 3

print(myTuple[2:5])
print(myTuple[:5:-1])

myTuple = ()
print(myTuple)

myTuple = (5,)

print((3, 4, 1) + (9, 8)) # (3, 4, 1, 9, 8)
print((1, 2) * 3) # (1, 2, 1, 2, 1, 2)

myTuple = (i for i in range(10))
print(myTuple)

myTuple = tuple(i for i in range(10))
print(myTuple)

myTuple = (1, 2, 3)
myTuple = (0, myTuple[1], myTuple[2])
print(myTuple)

#myTuple[2] = 10 # TypeError: 'tuple' object does not support item assignment

#matrix = [[j for j in range(10000)] for i in range(10000)] # 3700 MB-os ram igény
#print(matrix[3213][4324])
#input()

cella_indexek = [(4734, 8765), (9321, 7543)]
ertekek = [18, 99]