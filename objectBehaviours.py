from tkinter import *
from functools import partial

memory = 0


class Movement:
    def __init__(self, obj, coordinate_system):
        self.coordinate_system = coordinate_system
        self.obj = obj
        self.motion_selector()

    @staticmethod
    def drag_start(e):
        widget = e.widget
        widget.startX = e.x
        widget.startY = e.y

    @staticmethod
    def drag_motion(e):
        widget = e.widget
        x = widget.winfo_x() - widget.startX + e.x
        y = widget.winfo_y() - widget.startY + e.y
        widget.place(x=x, y=y)

    @staticmethod
    def delete_object(e):
        widget = e.widget
        widget.destroy()

    def motion_selector(self):
        self.obj.bind("<Button-1>", self.drag_start)
        self.obj.bind("<B1-Motion>", self.drag_motion)
        self.obj.bind("<Button-3>", self.delete_object)


class ObjectFeature:
    def __init__(self, obj, screen):
        self.obj = obj
        self.screen = screen
        self.objectFeatureTab = None
        self.trigger()

    def object_feature_tab_init(self, e):  # it creates the objectFeature adjustment tab on the right of the screen,
        self.objectFeatureTab = Frame(self.screen, bg="#141E27")
        self.objectFeatureTab.place(relx=0.9, rely=0, relwidth=0.1, relheight=1)
        self.input_area()

        close_btn = Button(self.objectFeatureTab, text="X", activebackground="#CD0404",
                           command=self.objectFeatureTab.destroy)
        close_btn.place(relx=0.75, rely=0, relwidth=0.2, relheight=0.04)

    def print_input(self, input_txt, frame):
        txt = input_txt.get(1.0, "end-1c")
        self.obj.config(text=txt)
        frame.destroy()

    def input_area(self):
        text_frame = Canvas(self.objectFeatureTab)
        text_frame.place(relx=0.05, rely=0.79, relheight=0.2, relwidth=0.9)
        input_txt = Text(text_frame)
        input_txt.insert(INSERT, self.obj.cget("text"))
        input_txt.place(relheight=0.8, relwidth=1)
        btn = Button(text_frame, text="✓", bg="#EEEDDE", activebackground="#203239",
                     command=partial(self.print_input, input_txt, text_frame))
        btn.place(rely=0.8, relheight=0.2, relwidth=1)

    def trigger(self):
        self.obj.bind("<Double-Button-1>", self.object_feature_tab_init)  # triggers the input screen


class Object:
    def __init__(self, obj, coordinate_system):
        self.coordinate_system = coordinate_system
        self.LinkedObjects = []
        self.Links = []
        self.obj = obj
        self.my_line = None
        self.id = id(obj)
        self.trigger()

    def first(self, e):
        global memory
        widget = e.widget
        widget.startX = widget.winfo_x()
        widget.startY = widget.winfo_y()
        memory = [widget.startX, widget.startY, self.id, self.Links]#first 2 ind = current coordinates of obj
                                                                    #third ind = objects's id
                                                                    #fourth ind = links that obj have
    def second(self, e):
        widget = e.widget
        print(f'comes {memory[2]}')
        print(f'goes {self.id}')
        self.my_line = self.coordinate_system.create_line(memory[0], memory[1], widget.winfo_x(), widget.winfo_y(),
                                                          fill="red", arrow="last", width=2)
        memory[3].append(self.my_line)
        self.Links.append(self.my_line)
        print(f'List of links of arrow goes to {self.Links}, list of links of arrow comes to : {memory[3]}')
        #self.coordinate_system.delete(self.my_line) ,, it is for deletion

    def trigger(self):
        self.obj.bind("<Shift-Button-1>", self.first)
        self.obj.bind("<Shift-Button-2>", self.second)

