from tkinter import *
import objectBehaviours
import GUI


class Triggers:
    def __init__(self, obj, screen):
        self.obj = obj
        self.screen = screen
        self.obj_label = obj.obj_label
        self.obj_isLink = obj.obj_isLink
        self.properties_frame = None
        self.line = None

        self.trigger()

    # TRIGGER FUNCTIONS #

    def drag_start(self, e):
        if self.properties_frame is not None:
            self.properties_frame.destroy()

        if not GUI.GUI.isLink:
            widget = e.widget
            widget.startX = e.x
            widget.startY = e.y

        else:
            if not self.obj_isLink:
                self.get_id(e)
            self.obj_isLink = False


    def drag_motion(self, e):
        if self.properties_frame is not None:
            self.properties_frame.destroy()

        if not GUI.GUI.isLink:
            widget = e.widget
            pos_x = widget.winfo_x()
            pos_y = widget.winfo_y()
            x = pos_x - widget.startX + e.x
            y = pos_y - widget.startY + e.y
            widget.place(x=x, y=y)
            self.obj.obj_pos_x = pos_x
            self.obj.obj_pos_y = pos_y

        for line in self.obj.obj_line:
            line.upgrade_line()

    def delete_object(self, e):
        if self.properties_frame is not None:
            self.properties_frame.destroy()

        if not GUI.GUI.isLink:
            widget = e.widget
            widget.destroy()

        for line in self.obj.obj_line:
            line.delete_line()

    def delete_l(self, event):
        for line in GUI.GUI.lines:
            if line.line == event.widget.find_closest(event.x, event.y)[0]:
                self.screen.delete(line.line)
                break

    def obj_properties_screen(self, e):
        if not GUI.GUI.isLink:
            widget = e.widget
            self.properties_frame = Frame(self.screen, bg="#141E27")
            self.properties_frame.place(relx=1, rely=0.5, relwidth=0.15, relheight=1, anchor=E)

            txt = objectBehaviours.TextInput(widget, self.properties_frame)
            txt.create_text()

            link_message = Label(self.properties_frame, text="Click for link", bg="#141E27", foreground="white")
            link_message.place(relx=0, rely=0.2, relwidth=1, relheight=0.025)

            link_btn = Button(self.properties_frame, text="Link", command=self.trigger_link)
            link_btn.place(relx=0.1, rely=0.23, relwidth=0.8, relheight=0.04)

            close_btn = Button(self.properties_frame, text="X", activebackground="#CD0404",
                               command=self.properties_frame.destroy)
            close_btn.place(relx=0.75, rely=0, relwidth=0.2, relheight=0.04)

    def get_id(self, e):
        if self.properties_frame is not None:
            self.properties_frame.destroy()

        widget = e.widget
        GUI.GUI.linked_obj.obj_links.append(id(widget))

        txt = GUI.GUI.linked_obj.obj_label.cget("text")

        pos_widget_x = widget.winfo_x()
        pos_widget_y = widget.winfo_y()

        for i in GUI.GUI.linked_obj.obj_links:
            print(txt + " | Link:", i, "\n")

        self.line = objectBehaviours.Line(self.screen, GUI.GUI.linked_obj, self.obj)

        self.obj.obj_line.append(self.line)
        GUI.GUI.linked_obj.obj_line.append(self.line)

        GUI.GUI.lines.append(self.line)
        print(GUI.GUI.lines)

        GUI.GUI.linked_obj = None
        GUI.GUI.isLink = False

    # TRIGGERS #

    def trigger_start(self):
        self.obj_label.bind("<Button-1>", self.drag_start)

    def trigger_motion(self):
        self.obj_label.bind("<B1-Motion>", self.drag_motion)

    def trigger_delete(self):
        self.obj_label.bind("<Button-3>", self.delete_object)

    def trigger_prop_screen(self):
        self.obj_label.bind("<Double-Button-1>", self.obj_properties_screen)

    def trigger_canvas(self):
        self.screen.bind("<Button-3>", self.delete_l)

    def trigger_link(self):
        self.obj_isLink = True
        GUI.GUI.linked_obj = self.obj
        GUI.GUI.isLink = True

    def trigger(self):
        self.trigger_start()
        self.trigger_motion()
        self.trigger_delete()
        self.trigger_canvas()
        self.trigger_prop_screen()
