from tkinter import *

root = Tk()
root.title("App")

frame1 = Frame(root, width=500, height=100, bg="darkblue")
frame2 = Frame(root, width=300, height=200, bg="green", bd=20)
frame3 = Frame(root, width=500, height=150, bg="yellow")
frame1.pack()
frame2.pack()
frame3.pack()

entry2 = Entry(frame2, width=20, bg="white")
entry2.pack()

# Добавление второго окна
window = Toplevel(root, relief=SUNKEN, bd=10, bg="lightblue")
window.title("Sub Window")
window.minsize(width=400, height=200)
window.mainloop()


root.mainloop()