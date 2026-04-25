# Task 1 - Length of items
myList = ["cat", "dog", "lion", "lizard", "kangaroo"]
dictionary = {}
for item in myList:
    dictionary[item] = len(item)
print(dictionary)

# Task 2 - Longest word
def longest_word():
    k = list(dictionary.keys())
    v = list(dictionary.values())
    maximum = v[0]
    max_index = 0
    for i in range(1, len(v)):
        if v[i] > maximum:
            maximum = v[i]
            max_index = i
    return k[max_index]

# Task 2 - Shorter version
def longest_word_2():
    k = list(dictionary.keys())
    v = list(dictionary.values())
    return k[v.index(max(v))]


print(longest_word())
print(longest_word_2())


# Task 3 - Uneven matrix
matrix = [[4, 23, 8], [2], [63, 4, 15, 16], [4, 7]]
max_len = 0
for row in matrix:
    for item in row:
        print(item, end=" ")
    print("")

for i in matrix:
    if len(i) > max_len:
        max_len = len(i)

for j in matrix:
    k = max_len - len(j)
    while k > 0:
        j.append(0)
        k -= 1
        
for row in matrix:
    for item in row:
        print(item, end=" ")
    print("")


# Task 4 - Find coordinates in matrix
num = int(input("What number are you looking for?\n"))
number_list = []
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == num:
            number_list.append([i, j])
for item in number_list:
    print(item)
if len(number_list) == 0:
    print("This number is not in the matrix.")
