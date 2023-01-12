import tkinter as tk


def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)

def label_motion(_label):
    _label.bind("<Button-1>",drag_start)
    _label.bind("<B1-Motion>",drag_motion)

def create_label(obj,screen):
    obj_img = tk.PhotoImage(file="images\\"+obj+".png")
    _label = tk.Label(screen, image=obj_img, bg="orange")
    _label.place(relx=0, rely=0)
    _label.bind("<Button-1>",drag_start)
    _label.bind("<B1-Motion>",drag_motion)

