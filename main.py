import tkinter as tk

window = tk.Tk()
button = tk.Button
frame = tk.Frame
menu = tk.Menu

rectangle_img = tk.PhotoImage(file="images\\rectangle.png")
arrow_img = tk.PhotoImage(file="images\\arrow.png")

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)

def create_label_rect():
    _label = tk.Label(frame_cordinate, image=rectangle_img)
    _label.place(relx=0, rely=0)
    _label.bind("<Button-1>",drag_start)
    _label.bind("<B1-Motion>",drag_motion)

def create_label_arrow():
    _label = tk.Label(frame_cordinate, image=arrow_img)
    _label.place(relx=0, rely=0)
    _label.bind("<Button-1>",drag_start)
    _label.bind("<B1-Motion>",drag_motion)



window.geometry("700x600+1200+80")
window.title("Graphical Modeling Editor")



frame_left = frame(window, bg="black")
frame_left.place(relx=0, rely=0, relwidth=0.1, relheight=1)
	

frame_cordinate = frame(window, bg="white")
frame_cordinate.place(relx=0.1, rely=0, relwidth=1, relheight=1)


button_rectangular = button(frame_left, text="rect", activebackground="grey", command=create_label_rect)
button_rectangular.place(relx=0.1, rely=0.1, relwidth=0.75, relheight=0.1)

button_arrow = button(frame_left, text="arrow", activebackground="grey", command=create_label_arrow)
button_arrow.place(relx=0.1, rely=0.3, relwidth=0.75, relheight=0.1)

### MENU ###
menubar = menu(window)
filemenu = menu(menubar, tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)
helpmenu = menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index")
helpmenu.add_command(label="About...")
menubar.add_cascade(label="Help", menu=helpmenu)
window.config(menu=menubar)


window.mainloop()

