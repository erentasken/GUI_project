from tkinter import *
from functools import partial


class Arrangement:
    def __init__(self, obj, screen):
        self.obj = obj
        self.screen = screen
        self.rearrange()

    def _printInput(self, inputTxt, frame):
        txt = inputTxt.get(1.0, "end-1c")
        self.obj.config(text=txt)
        frame.destroy()

    def create_text(self, e):
        textFrame = Canvas(self.screen, bg="black")
        textFrame.place(relx=0.4, rely=0.8, relheight=0.2, relwidth=0.4)

        inputTxt = Text(textFrame)
        inputTxt.place(relheight=0.8, relwidth=1)

        btn = Button(textFrame, text="✓", activebackground="#072B53",
                     command=partial(self._printInput, inputTxt, textFrame))
        btn.place(rely=0.8, relheight=0.2, relwidth=1)

    def rearrange(self):
        self.obj.bind("<Double-Button-1>", self.create_text)
