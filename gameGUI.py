import random
import tkinter
import numpy as np
size= 4
root = tkinter.Tk()
root.title("Sliding Tile")
array_num = np.arange(size * size)
num_list = array_num.tolist()
num_list.append(' ')
num_list.remove(0)
T = num_list
T2 = np.reshape(num_list, (-1, size))

random.shuffle(num_list)

T.append(' ')
T.remove(' ')
a = num_list.index(' ')

ec = a % size
er = int(a / size)
T = np.reshape(num_list, (-1, size))

global moves

moves=0
def update(event):
    for i in range(size):
        for j in range(size):
            if T[i][j]!=' ':
                blank = tkinter.Label(root, text=T[i][j],borderwidth=1, width=5, height=5, fg="white",bg="#32a895",
                                      font=('Monova', 25),padx=0)
                blank.grid(row=i, column=j)
            else:
                blank = tkinter.Label(root, text=T[i][j], borderwidth=1, width=5, height=5, fg="white", bg="white",
                                      font=('Monova', 25), padx=0)
                blank.grid(row=i, column=j)

def updateintro():
    for i in range(size):
        for j in range(size):
            if i!=1:
                blank = tkinter.Label(root, borderwidth=1, width=5, height=5, fg="white",bg="#32a895", font=('Monova', 25),padx=0)
                blank.grid(row=i, column=j)
    blank= tkinter.Label(root, borderwidth=1,text="Welcome", width=5, height=5, fg="white", bg="#32a895", font=('Monova', 25), padx=0)
    blank.grid(row=1, column=1)

def updatewin():
    for i in range(size):
        for j in range(size):
            if i!=1:
                blank = tkinter.Label(root, borderwidth=1, width=5, height=5, fg="white",bg="#32a895", font=('Monova', 25),padx=0)
                blank.grid(row=i, column=j)
    blank= tkinter.Label(root, borderwidth=1,text="you won", width=5, height=5, fg="white", bg="#32a895", font=('Monova', 25), padx=0)
    blank.grid(row=1, column=1)

def gstats():
    print(T)
    print(T2)
    if (T == T2).all():
        updatewin()
def mdown(event):
    global er,ec
    if (er+1)!=size:
        blank = tkinter.Label(root, borderwidth=1, text=T[er][ec], width=5, height=5, fg="black", bg="white",
                              font=('Monova', 25), padx=0)
        blank.grid(row=er+1, column=ec)
        blank = tkinter.Label(root, borderwidth=1, text=T[er+1][ec], width=5, height=5, fg="white", bg="#32a895",
                              font=('Monova', 25), padx=0)
        blank.grid(row=er, column=ec)
        T[er][ec], T[er+1][ec] = T[er+1][ec], T[er][ec]
        er = er + 1
    gstats()
def mup(event):
    global er,ec
    blank = tkinter.Label(root, borderwidth=1, text=T[er][ec], width=5, height=5, fg="black", bg="white",
                          font=('Monova', 25), padx=0)
    blank.grid(row=er - 1, column=ec)
    blank = tkinter.Label(root, borderwidth=1, text=T[er - 1][ec], width=5, height=5, fg="white", bg="#32a895",
                          font=('Monova', 25), padx=0)
    blank.grid(row=er, column=ec)
    T[er][ec], T[er-1][ec] = T[er-1][ec], T[er][ec]
    er = er - 1
    gstats()
def mleft(event):
    global er,ec
    blank = tkinter.Label(root, borderwidth=1, text=T[er][ec], width=5, height=5, fg="black", bg="white",
                          font=('Monova', 25), padx=0)
    blank.grid(row=er, column=ec - 1)
    blank = tkinter.Label(root, borderwidth=1, text=T[er][ec - 1], width=5, height=5, fg="white", bg="#32a895",
                          font=('Monova', 25), padx=0)
    blank.grid(row=er, column=ec)
    T[er][ec], T[er][ec - 1] = T[er][ec - 1], T[er][ec]
    ec = ec - 1
    gstats()
def mright(event):
    global er,ec
    if (ec+1)!=size:
        blank = tkinter.Label(root, borderwidth=1, text=T[er][ec], width=5, height=5, fg="black", bg="white",
                              font=('Monova', 25), padx=0)
        blank.grid(row=er, column=ec + 1)
        blank = tkinter.Label(root, borderwidth=1, text=T[er][ec + 1], width=5, height=5, fg="white", bg="#32a895",
                              font=('Monova', 25), padx=0)
        blank.grid(row=er, column=ec)
        T[er][ec], T[er][ec + 1] = T[er][ec + 1], T[er][ec]
        ec = ec + 1
        gstats()


updateintro()
root.bind('<Return>',update)
root.bind('<Up>',mup)
root.bind('<Down>',mdown)
root.bind('<Left>',mleft)
root.bind('<Right>',mright)
root.mainloop()