from tkinter import *

window = Tk()
window.geometry("500x500")
window.configure(background="grey")

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y
def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)

left_frame = Label(window, bg = "black", width = 15, height =1250)
left_frame.pack(side = LEFT)

label = Label(window, bg="red",width=10,height=5)
label.place(x = -15, y = 0)
label.pack(side = LEFT)
label2 = Label(window,bg="blue",width=10,height=5)
label2.place(x = 15, y = 0)
label2.pack(padx=25, pady =100)




label.bind("<Button-1>",drag_start)
label.bind("<B1-Motion>",drag_motion)
label2.bind("<Button-1>",drag_start)
label2.bind("<B1-Motion>",drag_motion)

window.mainloop()