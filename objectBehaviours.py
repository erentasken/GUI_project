from tkinter import *
from functools import partial
import ObjectTrigger


class Objects:
    def __init__(self, obj, screen):
        self.obj = obj
        self.screen = screen

        self.obj_img = None
        self.obj_label = None
        self.obj_txt = None
        self.long_edge = 300
        self.short_edge = 150
        self.obj_isLink = False
        self.obj_links = []

        self.create_label()

    def create_label(self):
        self.obj_img = PhotoImage(file="images\\" + self.obj + ".png")
        self.obj_label = Label(self.screen, image=self.obj_img, compound=CENTER)
        self.obj_label.img = self.obj_img
        self.obj_label.place(relx=0, rely=0)


class TextInput:
    def __init__(self, obj, screen):
        self.obj = obj
        self.screen = screen

    def printInput(self, inputTxt, frame):
        txt = inputTxt.get(1.0, "end-1c")
        self.obj.config(text=txt)
        frame.destroy()

    def create_text(self):
        textFrame = Canvas(self.screen)
        textFrame.place(relx=0.05, rely=0.79, relheight=0.2, relwidth=0.9)

        inputTxt = Text(textFrame)
        inputTxt.insert(INSERT, self.obj.cget("text"))
        inputTxt.place(relheight=0.8, relwidth=1)

        btn = Button(textFrame, text="✓", bg="#EEEDDE", activebackground="#203239",
                     command=partial(self.printInput, inputTxt, textFrame))
        btn.place(rely=0.8, relheight=0.2, relwidth=1)
