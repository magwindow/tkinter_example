from tkinter import * 

class Paint(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.brush_size = 10
        self.color = "red"
        
        self.setUI()
        
    def draw(self, event):
        self.canvas.create_oval(
            event.x - self.brush_size,
            event.y - self.brush_size,
            event.x + self.brush_size,
            event.y + self.brush_size,
            fill=self.color,
            outline=self.color)
        
    def set_color(self, new_color):
        '''Изменение цвета кисти'''
        self.color = new_color
        
    def set_brush_size(self, new_size):
        '''Изменение размера кисти'''
        self.brush_size = new_size
        
    def setUI(self):
        self.parent.title("Paint")
        self.pack(fill=BOTH, expand=1)
        self.columnconfigure(6, weight=1)
        self.rowconfigure(2, weight=1)
        self.canvas = Canvas(self, bg="white")
        self.canvas.grid(row=2, column=0, columnspan=7, padx=5, pady=5, sticky=E+W+S+N)
        self.canvas.bind("<B1-Motion>", self.draw)
        color_label = Label(self, text="Цвет: ")
        color_label.grid(row=0, column=0, padx=6)
        
        # Создание кнопок
        red_btn = Button(self, text="Красный", width=10, command=lambda: self.set_color("red"))
        red_btn.grid(row=0, column=1)
        green_btn = Button(self, text="Зеленый", width=10, command=lambda: self.set_color("green"))
        green_btn.grid(row=0, column=2)
        blue_btn = Button(self, text="Синий", width=10, command=lambda: self.set_color("blue"))
        blue_btn.grid(row=0, column=3)
        black_btn = Button(self, text="Черный", width=10, command=lambda: self.set_color("black"))
        black_btn.grid(row=0, column=4)
        white_btn = Button(self, text="Белый", width=10, command=lambda: self.set_color("white"))
        white_btn.grid(row=0, column=5)
        
        # Создаем метку для кнопок изменения размера кисти
        size_label = Label(self, text="Размер кисти: ")
        size_label.grid(row=1, column=0, padx=5)
        one_btn = Button(self, text="2x", width=10, command=lambda: self.set_brush_size(2))
        one_btn.grid(row=1, column=1)
        two_btn = Button(self, text="5x", width=10, command=lambda: self.set_brush_size(5))
        two_btn.grid(row=1, column=2)
        five_btn = Button(self, text="7x", width=10, command=lambda: self.set_brush_size(7))
        five_btn.grid(row=1, column=3)
        seven_btn = Button(self, text="10x", width=10, command=lambda: self.set_brush_size(10))
        seven_btn.grid(row=1, column=4)
        ten_btn = Button(self, text="20x", width=10, command=lambda: self.set_brush_size(20))
        ten_btn.grid(row=1, column=5)
        twenty_btn = Button(self, text="50x", width=10, command=lambda: self.set_brush_size(50))
        twenty_btn.grid(row=1, column=6, sticky=W)
        clear_btn = Button(self, text="Очистить", width=10, command=lambda: self.canvas.delete("all"))
        clear_btn.grid(row=0, column=6, sticky=W)
        

def main():
    root = Tk()
    root.geometry("800x600+300+100")
    Paint(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()