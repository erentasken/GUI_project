from tkinter import *
import LeftBar
import PlotScreen

window = Tk()

window.geometry("700x600+1200+80")
window.title("Graphical Modeling Editor")

plotScreen = PlotScreen.CoordinateScreen(window)
LeftBar.create_frame(window, plotScreen.coordinateSystem)

window.mainloop()