from tkinter import *
from tkinter import Canvas
from functools import partial
import objectBehaviours




class GUI:
    def __init__(self):
        self.coordinate_system = None
        self.objects = {"arrow", "rectangle"}  # list of shapes
        self.window = Tk()
        self.window.geometry("900x700+1000+80")
        self.window.title("Graphical Modeling Editor")
        self.coordinate_screen()#generates the right part of the screen
        self.create_frame(self.window)
        self.window.mainloop()
        self.memory= None

    def coordinate_screen(self):  # method for right part of the existing screen.
        self.coordinate_system = Canvas(self.window)
        self.coordinate_system.place(relx=0.1, rely=0, relwidth=0.9, relheight=1)

    def create_label(self, obj):
        obj_img = PhotoImage(file="images\\" + obj + ".png")
        label = Label(self.coordinate_system, image=obj_img, compound=CENTER)
        label.img = obj_img
        label.place(relx=0, rely=0)

        objectBehaviours.Object(label, self.coordinate_system)
        objectBehaviours.Movement(label, self.coordinate_system)
        objectBehaviours.ObjectFeature(label, self.coordinate_system)

    def create_frame(self, screen):  # creates left-column puts the object's buttons as well.
        frame_left = Frame(screen, bg="#141E27")
        frame_left.place(relx=0, rely=0, relwidth=0.1, relheight=1)
        btn_frame = Frame(frame_left, bg="#141E27")
        btn_frame.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.8)
        btn_frame.columnconfigure(0, weight=1)
        btn_frame.columnconfigure(1, weight=1)

        for index, obj in enumerate(self.objects): # enumerate built-in function provide us to use index variable which I had use in line 44
            button_obj = Button(btn_frame, text=obj, bg="#EEEDDE", activebackground="#203239",
                                command=partial(self.create_label, obj))
            button_obj.place(relwidth=0.5)
            button_obj.grid(row=index * 2, sticky=N + W + S + E)

