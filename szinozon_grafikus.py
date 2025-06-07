import random
import tkinter
import tkinter.messagebox

def generate_puzzle():
    puzzle = ""
    while len(puzzle) < 4:
        num = random.randint(1,8) # 8 különböző "szín" lehetséges
        if str(num) not in puzzle:
            puzzle += str(num)
    return puzzle

puzzle = generate_puzzle() # pl.: 5723
tippek_szama = 0

def check_tipp():
    tipp = "1234"
    if len(tipp) != 4 or not tipp.isdigit() or len(set(tipp)) != 4:
        tkinter.messagebox.showwarning("HIBA!", "4 különböző 1-8 közötti számjegyet adj meg!")
        return
    
    jo_szamok = 0
    jo_szamok_jo_helyen = 0
    for i in range(len(tipp)):
        if tipp[i] == puzzle[i]:
            jo_szamok_jo_helyen += 1
        elif tipp[i] in puzzle:
            jo_szamok += 1
    tippek_szama += 1
    if tipp == puzzle:
        pass
    else:
        pass
    
root = tkinter.Tk()
root.title("Színözön")

tkinter.Label(root, text="Adj meg 4 különböző 1-8 közötti számjegyet (pl.: 1234)!").pack(pady = 5, padx = 5)

textbox = tkinter.Entry(root)
textbox.pack(pady=5)
textbox.focus()

btn_guess = tkinter.Button(root, text = "Tippelés", command = check_tipp)
btn_guess.pack(pady = 5)

result_label = tkinter.Label(root, text= "", fg="green") # fg - betű színe
result_label.pack(pady = 5)

history = tkinter.Listbox(root, width = 50, height = 35)
history.pack(pady=10)

root.mainloop()