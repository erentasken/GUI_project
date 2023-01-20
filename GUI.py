from tkinter import *
from tkinter import Canvas
from functools import partial

import objectBehaviours


class GUI:
    isLink = False

    def __init__(self):

        self.coordinateSystem = None
        self.frame_left = None
        self.btn_frame = None
        self._label = None

        self.objects = {"arrow", "rectangle"}  # list of shapes

        self.window = Tk()
        self.window.geometry("900x700+1000+80")
        self.window.title("Graphical Modeling Editor")

        self.CoordinateScreen()
        self.create_frame()

        self.window.mainloop()

    def CoordinateScreen(self):  # method for right part of the existing screen.
        self.coordinateSystem = Canvas(self.window)
        self.coordinateSystem.place(relx=0.1, rely=0, relwidth=0.9, relheight=1)

    def create_obj(self, obj, screen):
        newObj = objectBehaviours.Objects(obj, screen)
        objectBehaviours.ObjectTrigger.Triggers(newObj, screen)

    def create_frame(self):  # creates left-column puts the object's buttons as well.
        col = 0
        row = 0
        self.frame_left = Frame(self.window, bg="#141E27")
        self.frame_left.place(relx=0, rely=0, relwidth=0.1, relheight=1)

        self.btn_frame = Frame(self.frame_left, bg="#141E27")
        self.btn_frame.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.8)

        self.btn_frame.columnconfigure(0, weight=1)
        self.btn_frame.columnconfigure(1, weight=1)

        for obj in self.objects:
            button_obj = Button(self.btn_frame, text=obj, bg="#EEEDDE", activebackground="#203239",
                                command=partial(self.create_obj, obj, self.coordinateSystem))
            button_obj.place(relwidth=0.5)
            button_obj.grid(row=int(row), column=col % 2, sticky=N + W + S + E)
            col += 1
            row += 0.5
