from tkinter import *

class Movement:
    def __init__(self, obj):
        self.obj = obj
        self.obj_motion()

    def drag_start(self, e):
        widget = e.widget
        widget.startX = e.x
        widget.startY = e.y

    def drag_motion(self, e):
        widget = e.widget
        x = widget.winfo_x() - widget.startX + e.x
        y = widget.winfo_y() - widget.startY + e.y
        widget.place(x=x, y=y)

    def delete_object(self, e):
        widget = e.widget
        widget.destroy()

    def obj_motion(self):
        self.obj.bind("<Button-1>", self.drag_start)
        self.obj.bind("<B1-Motion>", self.drag_motion)
        self.obj.bind("<Button-3>",self.delete_object)
