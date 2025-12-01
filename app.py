from tkinter import *

root = Tk()
root.title("App")

canvas = Canvas(root, width=500, height=500, bg="lightgray")
canvas.create_arc(200, 200, 300, 300, start=0, extent=180, fill="yellow", outline="black")
canvas.create_text(250, 250, text="Hello World!", font=("Arial", 20))
canvas.pack()

root.mainloop()