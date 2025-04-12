import random

board = [
    [" ", "1", "2", "3"],
    ["1", "-", "-", "-"],
    ["2", "-", "-", "-"],
    ["3", "-", "-", "-"]
]
gameOn = True
player_1_turn = True
against_computer = False
winner = "draw"

def show_board():
    for sor in board:
        print(f"{sor[0]} {sor[1]} {sor[2]} {sor[3]}")
        
def read_and_put_symbol():
    sor = 10
    oszlop = 10
    if player_1_turn or not against_computer:
        while sor > 3 or sor < 1 or oszlop > 3 or oszlop < 1 or board[sor][oszlop] != "-":
            sor = int(input("Adj meg egy sort!\n"))
            oszlop = int(input("Adj meg egy oszlopot!\n"))
    else:
        while sor > 3 or sor < 1 or oszlop > 3 or oszlop < 1 or board[sor][oszlop] != "-":
            sor = random.randint(1,3)
            oszlop = random.randint(1,3)
        
    if player_1_turn:
        board[sor][oszlop] = "X"
    else:
        board[sor][oszlop] = "O"

def check_for_win():
    # Sorok ellenőrzése:
    for i in range(1, 4):
        if board[i][1] == board[i][2] and board[i][2] == board[i][3] and board[i][2] != "-":
            return True
    
    # Oszlopok ellenőrzése:
    for j in range(1, 4):
        if board[1][j] == board[2][j] and board[2][j] == board[3][j] and board[2][j] != "-":
            return True
        
    # Átlók ellenőrzése:
    if board[1][1] == board[2][2] and board[2][2] == board[3][3] and board[2][2] != "-": # Főátló
        return True
    if board[3][1] == board[2][2] and board[2][2] == board[1][3] and board[2][2] != "-": # Mellékátló
        return True
    # Ha nem volt sehol egyezés, nincs nyertes
    return False
    
def check_for_draw():
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "-":
                return False
    return True

answer = input('Számítógép ellen szeretnél játszani? (igen/nem)\n')
if answer == "igen":
    against_computer = True

while gameOn:
    show_board()
    read_and_put_symbol()
    
    have_winner = check_for_win()
    if have_winner:
        if player_1_turn:
            winner = "X wins"
        else:
            winner = "O wins"
        gameOn = False
        
    if check_for_draw():
        gameOn = False
    
    player_1_turn = not player_1_turn

show_board()
print(winner)
