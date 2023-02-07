import os
import sys
import tkinter as tk
from Conversor import Conversor
from Operaciones import mostrar_frame


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('400x550+400+20')
        self.resizable(0, 0)
        ruta = self.ruta('image/beta_icono.ico')
        self.iconbitmap(ruta)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        mostrar_frame(self, Conversor)


if __name__=='__main__':
    app = App()
    app.mainloop()
