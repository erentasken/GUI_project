from functools import partial
import tkinter as tk
import ButtonActivity

button = tk.Button
frame = tk.Frame

objects = {"arrow","rectangle"}


def create_frame(window):
    j = 0
    frame_left = frame(window, bg="black")
    frame_left.place(relx=0, rely=0, relwidth=0.1, relheight=1)

    for i in objects:
        j += 0.2
        button_obj = button(frame_left, text=i, activebackground="grey", command = partial(ButtonActivity.create_label,i,window))
        button_obj.place(relx=0.1, rely=j, relwidth=0.75, relheight=0.1)
        

