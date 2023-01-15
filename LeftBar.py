from functools import partial
from tkinter import *
import ButtonActivity

objects = {"arrow", "rectangle"}


def create_frame(screen, plotScreen):
    j = 0
    frame_left = Frame(screen, bg="black")
    frame_left.place(relx=0, rely=0, relwidth=0.1, relheight=1)

    for i in objects:
        j += 0.2
        button_obj = Button(frame_left, text=i, activebackground="grey",
                            command=partial(ButtonActivity.create_label, i, plotScreen))
        button_obj.place(relx=0.1, rely=j, relwidth=0.75, relheight=0.1)
