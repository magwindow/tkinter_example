from tkinter import *

def new_win():
    window = Toplevel(root, relief=SUNKEN, bd=10, bg="lightblue")
    window.title("Sub Window")
    window.minsize(width=400, height=200)
    window.mainloop()
    
def close_win():
    root.destroy()
    

def about():
    win = Toplevel(root)
    lab = Label(win, text="About")
    lab.pack()


root = Tk()
root.title("App")

# создается объект Меню на главном окне
menu = Menu(root)
# окно конфигурируется с указанием меню для него
root.config(menu=menu)

# создается пункт меню с размещением на основном меню (menu)
filemenu = Menu(menu)
menu.add_cascade(label="Файл", menu=filemenu)
filemenu.add_command(label="Открыть")
filemenu.add_command(label="Создать", command=new_win)
filemenu.add_command(label="Сохранить")
filemenu.add_command(label="Выход", command=close_win)

# второй пункт меню
helpmenu = Menu(menu)
menu.add_cascade(label="Помощь", menu=helpmenu)
helpmenu.add_command(label="Справка")
helpmenu.add_command(label="0 программе", command=about)

submenu = Menu(filemenu)
filemenu.add_cascade(label="Подменю", menu=submenu)
submenu.add_command(label="Пункт подменю")

root.mainloop()