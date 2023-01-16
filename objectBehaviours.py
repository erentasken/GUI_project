from tkinter import *
from functools import partial


class Movement:
    def __init__(self, obj):
        self.square_clicks = 0
        self.obj = obj
        self.motion_selector()

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

    def motion_selector(self):
        self.obj.bind("<Button-1>", self.drag_start)
        self.obj.bind("<B1-Motion>", self.drag_motion)
        self.obj.bind("<Button-3>", self.delete_object)


class TextInput:
    def __init__(self, obj, screen):
        self.obj = obj
        self.screen = screen
        self.inputTrigger()

    def _printInput(self, inputTxt, frame):
        self.frame = frame
        txt = inputTxt.get(1.0, "end-1c")
        self.obj.config(text=txt)
        self.frame.destroy()

    def _create_text(self, e):
        textFrame = Canvas(self.screen)
        textFrame.place(relx=0.4, rely=0.8, relheight=0.2, relwidth=0.4)
        inputTxt = Text(textFrame)
        inputTxt.insert(INSERT, self.obj.cget("text"))
        inputTxt.place(relheight=0.8, relwidth=1)
        btn = Button(textFrame, text="✓", bg="#EEEDDE", activebackground="#203239",
                     command=partial(self._printInput, inputTxt, textFrame))
        btn.place(rely=0.8, relheight=0.2, relwidth=1)

    def inputTrigger(self):
        self.obj.bind("<Double-Button-1>", self._create_text)
