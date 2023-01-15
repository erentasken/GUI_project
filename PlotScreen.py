from tkinter import *


class CoordinateScreen:
    def __init__(self, screen):
        self.screen = screen
        self.coordinateSystem = Canvas
        self.create_screen()

    def create_screen(self):
        self.coordinateSystem = Canvas(self.screen)
        self.coordinateSystem.place(relx=0.1, rely=0, relwidth=0.9, relheight=1)

