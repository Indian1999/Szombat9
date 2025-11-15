board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0:
            print("■ " * 13)
        for j in range(len(board[i])):
            if j % 3 == 0:
                print("■ ", end="")
            print(board[i][j], end = " ")
        print("■")
    print("■ " * 13)

def solve(board):
    empty = find_empty(board)
    if empty == None:
        return True
    row = empty[0]
    col = empty[1]
    for num in range(1, 10):
        if valid(board, num, row, col):
            board[row][col] = num
            if solve(board):
                return True
            board[row][col] = 0
    return False
    
def valid(board, num, row, col):
    # Sorok ellenőrzése
    for i in range(len(board[row])):
        if board[row][i] == num:
            return False
        
    # Oszlopok ellenőrzése
    for i in range(len(board)):
        if board[i][col] == num:
            return False
        
    # Kis négyzetek ellenőrzése
    small_row = row // 3 * 3
    small_col = col // 3 * 3
    for i in range(small_row, small_row + 3):
        for j in range(small_col, small_col + 3):
            if board[i][j] == num:
                return False
    
    return True

    
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return [i, j]
    return None
    

print_board(board)
solve(board)
print("Megoldás:")
print_board(board)