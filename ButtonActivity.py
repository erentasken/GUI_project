from tkinter import *
import objectMovement

def create_label(obj, screen):
    obj_img = PhotoImage(file="images\\"+obj+".png")
    _label = Label(screen, image=obj_img)
    _label.img = obj_img 
    _label.place(relx=0, rely=0)
    move = objectMovement.Movement(_label)
