from tkinter import *

def colorR():
    frame.config(bg="red")
    
def colorG():
    frame.config(bg="green")
    
def colorB():
    frame.config(bg="blue")
    
def square():
    frame.config(width=640)
    frame.config(height=480)
    
def rectangle():
    frame.config(width=800)
    frame.config(height=600)
    
root = Tk()
root.title("App")

# Параметры окна по умолчанию - 300x100 и цвет фона - черный
frame = Frame(root, width=300, height=100, bg="black")
frame.pack()

menu = Menu(root)
root.config(menu=menu)

submenu = Menu(menu)
menu.add_cascade(label="Цвет", menu=submenu)
submenu.add_command(label="Красный", command=colorR)
submenu.add_command(label="Зеленый", command=colorG)
submenu.add_command(label="Синий", command=colorB)

submenu = Menu(menu)
menu.add_cascade(label="Форма", menu=submenu)
submenu.add_command(label="Квадрат", command=square)
submenu.add_command(label="Прямоугольник", command=rectangle)

root.mainloop()


