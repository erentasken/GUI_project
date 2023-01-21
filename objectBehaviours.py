from tkinter import *
from functools import partial


class Movement:
    def __init__(self, obj):
        self.square_clicks = 0
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


class TextInput:
    def __init__(self, obj, screen):
        self.obj = obj
        self.screen = screen
        self.trigger()

    def create_text(self, e):
        objectFeature(self.obj, self.screen)

    def trigger(self):
        self.obj.bind("<Double-Button-1>", self.create_text)  # triggers the input screen

class objectFeature:
    def __init__(self, obj, screen):
        self.obj = obj
        self.screen = screen
        self.objectFeatureTab = None
        self.trigger()

    def close_tab(self):  # closes the tab (triggers from objectFeatureTabInit() function)
        self.objectFeatureTab.destroy()

    def object_feature_tab_init(self, e):  # it creates the objectFeature adjustment tab on the right of the screen,
        self.objectFeatureTab = Frame(self.screen, bg="#141E27")
        self.objectFeatureTab.place(relx=0.9, rely=0, relwidth=0.1, relheight=1)
        self.input_area()

        close_btn = Button(self.objectFeatureTab, text="X", bg="gray", fg='white', font=("Arial", 12, 'bold'), width=2,
                           height=1, command=self.close_tab)  # close button for closing that tab.
        close_btn.place(relx=0.95, rely=0.05, anchor='ne')

    def print_input(self, inputTxt, frame):
        self.frame = frame
        txt = inputTxt.get(1.0, "end-1c")
        self.obj.config(text=txt)
        self.frame.destroy()

    def input_area(self):
        textFrame = Canvas(self.objectFeatureTab)
        textFrame.place(relx=0.2, rely=0.2, relheight=0.2, relwidth=0.7)
        inputTxt = Text(textFrame)
        inputTxt.insert(INSERT, self.obj.cget("text"))
        inputTxt.place(relheight=0.8, relwidth=1)
        btn = Button(textFrame, text="✓", bg="#EEEDDE", activebackground="#203239",
                     command=partial(self.print_input, inputTxt, textFrame))
        btn.place(rely=0.8, relheight=0.2, relwidth=1)

    def trigger(self):
        self.obj.bind("<Double-Button-1>", self.object_feature_tab_init)  # triggers the input screen
