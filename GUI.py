from tkinter import *
from tkinter import Canvas
from functools import partial
import objectBehaviours


class GUI:
    def __init__(self):
        self.objects = {"arrow", "rectangle"}  # list of shapes
        self.window = Tk()
        self.window.geometry("900x700+1000+80")
        self.window.title("Graphical Modeling Editor")
        self.CoordinateScreen()
        self.create_frame(self.window, self.coordinateSystem, self.objects)
        self.window.mainloop()

    def CoordinateScreen(self):  # method for right part of the existing screen.
        self.coordinateSystem = Canvas(self.window)
        self.coordinateSystem.place(relx=0.1, rely=0, relwidth=0.9, relheight=1)

    def create_label(self, obj, screen):
        self.obj = obj
        self.screen = screen
        obj_img = PhotoImage(file="images\\" + self.obj + ".png")
        _label = Label(self.screen, image=obj_img, compound=CENTER)
        _label.img = obj_img
        _label.place(relx=0, rely=0)
        objectBehaviours.Movement(_label)
        objectBehaviours.objectFeature(_label, self.screen)

    def create_frame(self, screen, plotScreen, objects):  # creates left-column puts the object's buttons as well.
        col = 0
        row = 0
        frame_left = Frame(screen, bg="#141E27")
        frame_left.place(relx=0, rely=0, relwidth=0.1, relheight=1)
        btn_frame = Frame(frame_left, bg="#141E27")
        btn_frame.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.8)
        btn_frame.columnconfigure(0, weight=1)
        btn_frame.columnconfigure(1, weight=1)

        for obj in objects:
            button_obj = Button(btn_frame, text=obj, bg="#EEEDDE", activebackground="#203239",
                                command=partial(self.create_label, obj, plotScreen))
            button_obj.place(relwidth=0.5)
            button_obj.grid(row=int(row), column=col % 2, sticky=N + W + S + E)
            col += 1
            row += 0.5
