from tkinter import *

def b1(event):
    root.title("Button-1")
    print("Button-1")
    print(event.x, event.y)

def b3(event):
    root.title("Button-3")
    print("Button-3")
    print(event.x, event.y)

def move(event):
    root.title("Move")
    print("Move")
    print(event.x, event.y)


root = Tk()
root.title("App")
root.minsize(width=400, height=200)

root.bind("<Button-1>", b1)
root.bind("<Button-3>", b3)
root.bind("<Motion>", move)

root.mainloop()