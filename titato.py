#importing required modules
from tkinter import *
import customtkinter

#setting the appearance
customtkinter.set_appearance_mode("system")  # default
customtkinter.set_appearance_mode("dark")

app = customtkinter.CTk()
app.geometry("600x500")
app.title("TicTacToe Game")

n = 0
a = {}

for i in range(9):
    a[i] = ""

def endgame():
    app.destroy()


def end(p, c):
    for btn in [b1, b2, b3, b4, b5, b6, b7, b8, b9, clear_btn]:
        btn.configure(state="disabled")

    win_lebo = customtkinter.CTkLabel(app, text="Game Over", font=("verdana", 24))
    win_lebo.pack(pady=20)

    if p:
        winner_lebo = customtkinter.CTkLabel(app, text=f'"{p}" player {c}', font=("verdana", 16))
        (winner_lebo.pack(pady=20))
    else:
        winner_lebo = customtkinter.CTkLabel(app, text=f"It's a {c}", font=("verdana", 16))
        (winner_lebo.pack(pady=20))

    #frame2 = customtkinter.CTkFrame(app, fg_color="transparent")
    #frame2.pack(pady=10)

    #btn1 = customtkinter.CTkButton(frame2, text="Restart", fg_color="blue", command=restart)
    #btn1.grid(row=0, column=0, padx=(5, 10), pady=10)

    btn2 = customtkinter.CTkButton(app, text="End Game", fg_color="red",
                                   command=endgame)
    #btn2.grid(row=0, column=1, padx=(0, 10), pady=10)
    btn2.pack(pady=10)
    #end_note()
    #win_lebo.configure(text="Game Over", font=("verdana", 18))


def win():
    nn = 0

    for play in ("O", "X"):
        #horizontal
        if a[0] == play and a[1] == play and a[2] == play:
            b1.configure(fg_color="red")
            b2.configure(fg_color="red")
            b3.configure(fg_color="red")
            #winner(play)
            end(play, "won")
            break
        elif a[3] == play and a[4] == play and a[5] == play:
            b4.configure(fg_color="red")
            b5.configure(fg_color="red")
            b6.configure(fg_color="red")
            #winner(play)
            end(play, "won")
            break
        elif a[6] == play and a[7] == play and a[8] == play:
            b7.configure(fg_color="red")
            b8.configure(fg_color="red")
            b9.configure(fg_color="red")
            #winner(play)
            end(play, "won")
            break
        #vertical
        elif a[0] == play and a[3] == play and a[6] == play:
            b1.configure(fg_color="red")
            b4.configure(fg_color="red")
            b7.configure(fg_color="red")
            #winner(play)
            end(play, "won")
            break
        elif a[1] == play and a[4] == play and a[7] == play:
            b2.configure(fg_color="red")
            b5.configure(fg_color="red")
            b8.configure(fg_color="red")
            #winner(play)
            end(play, "won")
            break
        elif a[2] == play and a[5] == play and a[8] == play:
            b3.configure(fg_color="red")
            b6.configure(fg_color="red")
            b9.configure(fg_color="red")
            #winner(play)
            end(play, "won")
            break
        #diagonal
        elif a[0] == play and a[4] == play and a[8] == play:
            b1.configure(fg_color="red")
            b5.configure(fg_color="red")
            b9.configure(fg_color="red")
            #winner(play)
            end(play, "won")
            break
        elif a[2] == play and a[4] == play and a[6] == play:
            b3.configure(fg_color="red")
            b5.configure(fg_color="red")
            b7.configure(fg_color="red")
            #winner(play)
            end(play, "won")
            break
        else:
            # calling the draw
            for value in a.values():
                if value:
                    nn +=1
            if nn == 9:
                end("", "draw")

def click(b):
    global n
    global a
    n += 1


    if n % 2 == 0:
        tt = "X"
    else:
        tt = "O"

    if b == 1:
        b1.configure(text=tt)
        a[0] = b1.cget("text")
    if b == 2:
        b2.configure(text=tt)
        a[1] = b2.cget("text")
    if b == 3:
        b3.configure(text=tt)
        a[2] = b3.cget("text")
    if b == 4:
        b4.configure(text=tt)
        a[3] = b4.cget("text")
    if b == 5:
        b5.configure(text=tt)
        a[4] = b5.cget("text")
    if b == 6:
        b6.configure(text=tt)
        a[5] = b6.cget("text")
    if b == 7:
        b7.configure(text=tt)
        a[6] = b7.cget("text")
    if b == 8:
        b8.configure(text=tt)
        a[7] = b8.cget("text")
    if b == 9:
        b9.configure(text=tt)
        a[8] = b9.cget("text")

    #calling the win function
    win()

def clear():
    global n
    n = 0

    for i in [b1, b2, b3, b4, b5, b6, b7, b8, b9]:
        i.configure(text="")

    for i in range(9):
        a[i] = ""

tt = 'Click any box below to play the game of "X" and "O".'

lebo = customtkinter.CTkLabel(app, text=tt, font=("verdana", 18), text_color="white")
lebo.pack(pady=20)

frame = customtkinter.CTkFrame(app, height=300, width=300, border_color="red", border_width=2)
frame.pack(pady=10)

#the buttons to play the game
b1 = customtkinter.CTkButton(master=frame, text="", font=("verdana", 18),
                             width=50, corner_radius=0, command=lambda: click(1))
b1.grid(row=0, column=0, pady=(20, 0), padx=(10, 0))
b2 = customtkinter.CTkButton(master=frame, text="", font=("verdana", 18),
                             width=50, corner_radius=0, command=lambda: click(2))
b2.grid(row=0, column=1, pady=(20, 0))
b3 = customtkinter.CTkButton(master=frame, text="", font=("verdana", 18),
                             width=50, corner_radius=0, command=lambda: click(3))
b3.grid(row=0, column=2, pady=(20, 0), padx=(0, 10))
b4 = customtkinter.CTkButton(master=frame, text="", font=("verdana", 18),
                             width=50, corner_radius=0, command=lambda: click(4))
b4.grid(row=1, column=0, padx=(10,0))
b5 = customtkinter.CTkButton(master=frame, text="", font=("verdana", 18),
                             width=50, corner_radius=0, command=lambda: click(5))
b5.grid(row=1, column=1)
b6 = customtkinter.CTkButton(master=frame, text="", font=("verdana", 18),
                             width=50, corner_radius=0, command=lambda: click(6))
b6.grid(row=1, column=2, padx=(0, 10))
b7 = customtkinter.CTkButton(master=frame, text="", font=("verdana", 18),
                             width=50, corner_radius=0, command=lambda: click(7))
b7.grid(row=2, column=0, padx=(10, 0), pady=(0, 20))
b8 = customtkinter.CTkButton(master=frame, text="", font=("verdana", 18),
                             width=50, corner_radius=0, command=lambda: click(8))
b8.grid(row=2, column=1, pady=(0, 20))
b9 = customtkinter.CTkButton(master=frame, text="", font=("verdana", 18),
                             width=50, corner_radius=0, command=lambda: click(9))
b9.grid(row=2, column=2, padx=(0, 10), pady=(0, 20))

clear_btn = customtkinter.CTkButton(master=app, text="Clear", fg_color="red", command=clear)
clear_btn.pack(pady=20)

#win_lebo = customtkinter.CTkLabel(app, text="")
#win_lebo.pack(pady=20)

app.mainloop()
