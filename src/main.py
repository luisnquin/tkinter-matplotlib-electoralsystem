from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter import *

from databasef.db import DatabaseConnection



class ElectoralSystem(DatabaseConnection):
    def __init__(self):
        super().__init__()

        self.root = Tk()
        self.root.title("Sistema electoral")
        self.root.iconbitmap("assets/elec-sys.ico")
        self.root.geometry("1280x720")

        self.body()

        self.root.mainloop()

    def body(self):
        # TITLE        
        Frame(self.root, bg="#817985", width=1280, height=110).place(x=0, y=0)
        Label(self.root, text="SISTEMA ELECTORAL", bg="#817985", font=("Helvetica", 26), fg="#ffffff").place(x=130, y=20)
        # GRAPHICS

        Label(self.root, text="BARRA DE PRESIDENTES", font=("Helvetica", 18)).place(x=50, y=130)
        self.presidentGraphic()
        Label(self.root, text="BARRA DE VICEPRESIDENTES", font=("Helvetica", 18)).place(x=50, y=430)
        self.vicepresidentGraphic()

        # SEPARATOR
        Frame(self.root, width=2, height=500, bg="#000000").place(x=650, y=150)
        
        # FORMULARY
        Label(self.root, text="Ingrese su número de cédula: ", font=("Helvetica", 18)).place(x=700, y=150)
        formEntry = Entry(self.root, width=18, font=("Helvetica", 25))
        formEntry.place(x=700, y=200)

        Label(self.root, text="Presidente a elegir: ", font=("Helvetica", 18)).place(x=700, y=300)
        presidentCombox = Combobox(self.root, state="readonly", width=25, font=("Helvetica", 18))
        presidentCombox["values"] = ["Guillermo Lasso", "Segundo Andres Arauz", "Cynthia Viteri"]
        presidentCombox.place(x=700, y=350)

        Label(self.root, text="Vicepresidente a elegir: ", font=("Helvetica", 18)).place(x=700, y=400)
        vicepresidentCombox = Combobox(self.root, state="readonly", width=25, font=("Helvetica", 18))
        vicepresidentCombox["values"] = ["Doris Quiroz", "Ramiro Aguilar", "Jorge Glas"]
        vicepresidentCombox.place(x=700, y=450)

        def insertFormData():
            if formEntry.get() and presidentCombox.get() and vicepresidentCombox.get():
                self.receivedData[0] = formEntry.get()
                self.receivedData[1] = presidentCombox.get()
                self.receivedData[2] = vicepresidentCombox.get()

                self.insertOneData()
                
                if self.flag:
                    self.presidentGraphic()
                    self.vicepresidentGraphic()

                    formEntry.delete(0, END)
                else:
                    self.flag = True
            else:
                messagebox.showwarning("Advertencia", "Verifica que los datos del formulario estén completos.")


        theButton = Button(self.root, text="Enviar voto", command=lambda:insertFormData())
        theButton.config(bg="#bd3338", fg="#ffffff", font=("Helvetica", 18), width=20)
        theButton.place(x=720, y=530)

    def presidentGraphic(self):
        presidentGraphic = Frame(self.root, width=550, height=320)
        presidentGraphic.place(x=10, y=180)

        fig, axs = plt.subplots(dpi=60, figsize=(8, 4), sharey=True, facecolor="#e8e8e8")

        self.getCountPresidents()
        
        axs.bar(
            ["Guillermo Lasso", "Segundo Andres Arauz", "Cynthia Viteri"],
            [self.countPre[0], self.countPre[1], self.countPre[2]],
            color=["#022436", "#4a1146", "#8f0013"],
        )

        canvas = FigureCanvasTkAgg(fig, master=presidentGraphic)
        canvas.draw()
        canvas.get_tk_widget().place(x=0, y=0)

    def vicepresidentGraphic(self):
        vicepresidentGraphic = Frame(self.root, width=550, height=320)
        vicepresidentGraphic.place(x=10, y=480)

        fig, axs = plt.subplots(dpi=60, figsize=(8, 4), sharey=True, facecolor="#e8e8e8")

        self.getCountVicepre()

        axs.bar(
            ["Doris Quiroz", "Ramiro Aguilar", "Jorge Glas"],
            [self.countVicepre[0], self.countVicepre[1], self.countVicepre[2]],
            color=["#022436", "#4a1146", "#8f0013"],
        )

        canvas = FigureCanvasTkAgg(fig, master=vicepresidentGraphic)
        canvas.draw()
        canvas.get_tk_widget().place(x=0, y=0)


if __name__ == "__main__":
    ElectoralSystem()
