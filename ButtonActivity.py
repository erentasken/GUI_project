from tkinter import *
import objectMovement

def create_label(obj, screen):
    obj_text = "a"

    obj_img = PhotoImage(file="images\\"+obj+".png")
    _label = Label(screen, text=obj_text, image=obj_img, compound=CENTER)
    _label.img = obj_img 
    _label.place(relx=0, rely=0)
    move = objectMovement.Movement(_label)