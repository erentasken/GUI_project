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
        self.obj_pos_x = None
        self.obj_pos_y = None
        self.long_edge = 300
        self.short_edge = 150
        self.obj_isLink = False
        self.obj_links = []
        self.obj_line = []
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
        self.input_txt = None

    def print_input(self, text_frame):
        txt = self.input_txt.get(1.0, "end-1c")
        self.obj.config(text=txt)
        text_frame.destroy()

    def create_text(self):
        text_frame = Canvas(self.screen)
        text_frame.place(relx=0.05, rely=0.79, relheight=0.2, relwidth=0.9)
        self.input_txt = Text(text_frame)
        self.input_txt.insert(INSERT, self.obj.cget("text"))
        self.input_txt.place(relheight=0.8, relwidth=1)
        btn = Button(text_frame, text="✓", bg="#EEEDDE", activebackground="#203239",
                     command=partial(self.print_input, text_frame))
        btn.place(rely=0.8, relheight=0.2, relwidth=1)

class Link:
    def __init__(self, screen, start_obj, des_obj):
        self.screen = screen
        self.start_obj = start_obj
        self.des_obj = des_obj
        self.line = None
        self.create_link()

    def create_link(self):
        self.line = self.screen.create_line(self.start_obj.obj_pos_x, self.start_obj.obj_pos_y, self.des_obj.obj_pos_x,
                                            self.des_obj.obj_pos_y, fill="black", arrow="last", width=2)

    def update_link(self):
        self.screen.coords(self.line, self.start_obj.obj_pos_x, self.start_obj.obj_pos_y, self.des_obj.obj_pos_x,
                           self.des_obj.obj_pos_y)

    def delete_link(self):
        self.screen.delete(self.line)
