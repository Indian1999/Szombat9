import random

board = [
    [" ", "1", "2", "3"],
    ["1", "-", "-", "-"],
    ["2", "-", "-", "-"],
    ["3", "-", "-", "-"]
]
gameOn = True
player_1_turn = True
winner = "draw"

def show_board():
    for sor in board:
        print(f"{sor[0]} {sor[1]} {sor[2]} {sor[3]}")
        
def read_and_put_symbol():
    sor = 10
    oszlop = 10
    while sor > 3 or sor < 1 or oszlop > 3 or oszlop < 1 or board[sor][oszlop] != "-":
        sor = int(input("Adj meg egy sort!\n"))
        oszlop = int(input("Adj meg egy oszlopot!\n"))
        
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
    
while gameOn:
    show_board()
    read_and_put_symbol()
    
    have_winner = check_for_win()
    print(have_winner)
    
    player_1_turn = not player_1_turn
