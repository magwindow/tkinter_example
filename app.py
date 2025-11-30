from tkinter import * 

def hello(event):
    print("Hello World")

root = Tk()
root.title("App")
root.geometry("300x400")

btn = Button(root, text="Click", width=10, height=2, fg="white", bg="blue")
btn.bind("<Button-1>", hello)
btn.pack()

root.mainloop()