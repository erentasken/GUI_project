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
        self.trigger_bindings()

    def drag_start(self, e):
        if self.properties_frame is not None:
            self.properties_frame.destroy()
        if not GUI.Gui.isLink:
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
        if not GUI.Gui.isLink:
            widget = e.widget
            pos_x = widget.winfo_x()
            pos_y = widget.winfo_y()
            x = pos_x - widget.startX + e.x
            y = pos_y - widget.startY + e.y
            widget.place(x=x, y=y)
            self.obj.obj_pos_x = pos_x
            self.obj.obj_pos_y = pos_y
        for line in self.obj.obj_line:
            line.update_link()

    def delete_object(self, e):
        if self.properties_frame is not None:
            self.properties_frame.destroy()
        if not GUI.Gui.isLink:
            widget = e.widget
            widget.destroy()
        for line in self.obj.obj_line:
            line.delete_link()

    def delete_link(self, event):
        for line in GUI.Gui.lines:
            if line.line == event.widget.find_closest(event.x, event.y)[0]:
                self.screen.delete(line.line)
                break

    def obj_properties_screen(self, e):
        if not GUI.Gui.isLink:
            widget = e.widget
            self.properties_frame = Frame(self.screen, bg="#141E27")
            self.properties_frame.place(relx=1, rely=0.5, relwidth=0.15, relheight=1, anchor=E)
            txt = objectBehaviours.TextInput(widget, self.properties_frame)
            txt.create_text()
            link_message = Label(self.properties_frame, text="Click for link", bg="#141E27", foreground="white")
            link_message.place(relx=0, rely=0.2, relwidth=1, relheight=0.025)
            link_btn = Button(self.properties_frame, text="Link", command=self.set_as_link)
            link_btn.place(relx=0.1, rely=0.23, relwidth=0.8, relheight=0.04)
            close_btn = Button(self.properties_frame, text="X", activebackground="#CD0404",
                               command=self.properties_frame.destroy)
            close_btn.place(relx=0.75, rely=0, relwidth=0.2, relheight=0.04)

    def get_id(self, e):
        if self.properties_frame is not None:
            self.properties_frame.destroy()
        widget = e.widget
        GUI.Gui.linked_obj.obj_links.append(id(widget))
        txt = GUI.Gui.linked_obj.obj_label.cget("text")
        pos_widget_x = widget.winfo_x()
        pos_widget_y = widget.winfo_y()
        self.line = objectBehaviours.Link(self.screen, GUI.Gui.linked_obj, self.obj)
        self.obj.obj_line.append(self.line)
        GUI.Gui.linked_obj.obj_line.append(self.line)
        GUI.Gui.lines.append(self.line)
        GUI.Gui.linked_obj = None
        GUI.Gui.isLink = False

    def trigger_bindings(self):
        self.obj_label.bind("<Button-1>", self.drag_start)
        self.obj_label.bind("<B1-Motion>", self.drag_motion)
        self.obj_label.bind("<Button-3>", self.delete_object)
        self.screen.bind("<Button-3>", self.delete_link)
        self.obj_label.bind("<Double-Button-1>", self.obj_properties_screen)

    def set_as_link(self):
        self.obj_isLink = True
        GUI.Gui.linked_obj = self.obj
        GUI.Gui.isLink = True
