from tkinter import *
import objectBehaviours


class Triggers:
    def __init__(self, obj, screen):
        self.obj = obj
        self.screen = screen
        self.trigger()

    ### TRIGGER FUNCTIONS ###

    def drag_start(self, e):
        widget = e.widget
        widget.startX = e.x
        widget.startY = e.y

    def drag_motion(self, e):
        widget = e.widget
        x = widget.winfo_x() - widget.startX + e.x
        y = widget.winfo_y() - widget.startY + e.y
        widget.place(x=x, y=y)

    def delete_object(self, e):
        widget = e.widget
        widget.destroy()

    def obj_properties_screen(self, e):
        widget = e.widget
        properties_frame = Frame(self.screen, bg="#141E27")
        properties_frame.place(relx=1, rely=0.5, relwidth=0.15, relheight=1, anchor=E)

        txt = objectBehaviours.TextInput(widget, properties_frame)
        txt.create_text()

        link_message = Label(properties_frame, text="Click for link", bg="#141E27", foreground="white")
        link_message.place(relx=0, rely=0.2, relwidth=1, relheight=0.025)

        link_btn = Button(properties_frame, text="Link", command=self.trigger_link)
        link_btn.place(relx=0.1, rely=0.23, relwidth=0.8, relheight=0.04)

        close_btn = Button(properties_frame, text="X", activebackground="#CD0404", command=properties_frame.destroy)
        close_btn.place(relx=0.75, rely=0, relwidth=0.2, relheight=0.04)

    def get_id(self, e):
        print("hello")
        """widget = e.widget
        self.links.append(id(widget))"""

    ### TRIGGERS ###

    def trigger_start(self):
        self.obj.bind("<Button-1>", self.drag_start)

    def trigger_motion(self):
        self.obj.bind("<B1-Motion>", self.drag_motion)

    def trigger_delete(self):
        self.obj.bind("<Button-3>", self.delete_object)

    def trigger_prop_screen(self):
        self.obj.bind("<Double-Button-1>", self.obj_properties_screen)

    def trigger_link(self):
        self.obj.bind("<Button-1>", self.get_id) #there is error

    def trigger(self):
        self.trigger_start()
        self.trigger_motion()
        self.trigger_delete()
        self.trigger_prop_screen()
