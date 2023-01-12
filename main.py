import tkinter as tk
import LeftBar

window = tk.Tk()

window.geometry("700x600+1200+80")
window.title("Graphical Modeling Editor")

LeftBar.create_frame(window)

window.mainloop()