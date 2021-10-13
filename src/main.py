from tkinter.ttk import Combobox
from tkinter import *

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from pandas import DataFrame

class ElectoralSystem:
    def __init__(self):
        self.root = Tk()
        self.root.title("Sistema electoral")
        self.root.iconbitmap("assets/elec-sys.ico")
        self.root.geometry("1200x700")

        self.body()

        self.root.mainloop()

    def body(self):
        Label(self.root, text="SISTEMA ELECTORAL", font=("Helvetica", 26)).place(x=50, y=50)
        Label(self.root, text="Presidentes", font=("Helvetica", 18)).place(x=50, y=150)
        presidentGraphic = Frame(bg="#949292", width=215, height=620)
        presidentGraphic.place(x=50, y=200)

        Data1 = {"Presidentes": ['A', 'B'], 'Elecciones': [50, 24]}
        df1 = DataFrame(Data1, columns = ['Presidentes', 'Elecciones'])
        df1 = df1[['Presidentes', 'Elecciones']].groupby('Presidentes').sum()

        graphic1 = plt.Figure(figsize=(6, 5), dpi=50)
        bars = graphic1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(graphic1, presidentGraphic)
        bar1.get_tk_widget().pack(side=LEFT, fill=BOTH)
        df1.plot(kind='bar', legend=True, ax=bars)
        bars.set_title('Presidente')
        
        Label(self.root, text="Vicepresidentes", font=("Helvetica", 18)).place(x=50, y=450)
        # FREE SPACE

        Frame(self.root, width=2, height=500, bg="#000000").place(x=650, y=150)
        Label(self.root, text="Ingrese su número de cédula: ", font=("Helvetica", 18)).place(x=700, y = 150)
        Entry(self.root, width=18, font=("Helvetica", 25)).place(x=700, y=200)
        Label(self.root, text="Presidente a elegir: ", font=("Helvetica", 18)).place(x=700, y = 350)
        presidentCombox = Combobox(self.root, state="readonly", width=25, font=("Helvetica", 18))
        presidentCombox["values"] = ["Guillermo Lasso", "Segundo Andres Arauz", "Cynthia Viteri"]
        presidentCombox.place(x=700, y=400)

        Label(self.root, text="Vicepresidente a elegir: ", font=("Helvetica", 18)).place(x=700, y = 550)
        vicepresidentCombox = Combobox(self.root, state="readonly", width=25, font=("Helvetica", 18))
        vicepresidentCombox["values"] = ["Doris Quiroz", "Ramiro Aguilar", "Jorge Glas"]
        vicepresidentCombox.place(x=700, y=600)



if __name__ == '__main__':
    ElectoralSystem()