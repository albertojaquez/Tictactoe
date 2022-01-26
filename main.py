import time
import tkinter as tk
from tkinter import ttk

#Frame
ventanaInicio = tk.Tk()
ventanaInicio.title("Tic Tac Toe")
ventanaInicio.configure(bg='black')
ventanaInicio.geometry("300x400+618+232")

FondBoton=ttk.Style()
FondBoton.configure("MyButton.TButton",font=("Times",15))

def JugarJ2():

    def BotonRegresar():
        BotonJugarCPU.place(x=25, y=150, width=250, height=35)
        BotonJugarJ2.place(x=25, y=190, width=250, height=35)
        BotonSalir.place(x=25, y=230, width=250, height=35)
        BotonRegresar.place_forget()

    time.sleep(0.1)
    BotonSalir.place_forget()
    BotonJugarCPU.place_forget()
    BotonJugarJ2.place_forget()

    BotonRegresar = ttk.Button(ventanaInicio, text="Regresar", style="MyButton.TButton", command=BotonRegresar)
    BotonRegresar.place(x=190, y=355, width=100, height=35)

def JugarCPU():

    def BotonRegresar():
        BotonJugarCPU.place(x=25, y=150, width=250, height=35)
        BotonJugarJ2.place(x=25, y=190, width=250, height=35)
        BotonSalir.place(x=25, y=230, width=250, height=35)
        BotonRegresar.place_forget()

    time.sleep(0.1)
    BotonSalir.place_forget()
    BotonJugarCPU.place_forget()
    BotonJugarJ2.place_forget()

    BotonRegresar = ttk.Button(ventanaInicio, text="Regresar", style="MyButton.TButton", command=BotonRegresar)
    BotonRegresar.place(x=190, y=355, width=100, height=35)

#Function to play
def SalirJuego():
    ventanaInicio.destroy()
#def ventanaJugar():
#    if BotonSalir.winfo_ismapped():
#        BotonSalir.place_forget()
#    else:
#        BotonSalir.place(x=25, y=190, width=250, height=35)
#LogoJuego=tkinter.Label(ventanaInicio,image=tkinter.PhotoImage(file="LogoNombre.jpg"))
#LogoJuego.pack()

#Create button to play with CPU
BotonJugarCPU = ttk.Button(ventanaInicio,text="J1vs CPU",style="MyButton.TButton",command=JugarCPU)
BotonJugarCPU.place(x=25,y=150,width=250,height=35)

#Create button to play with a friend
BotonJugarJ2=ttk.Button(ventanaInicio,text="J1 vs J2",style="MyButton.TButton",command=JugarJ2)
BotonJugarJ2.place(x=25,y=190,width=250,height=35)

#Create button to quit
BotonSalir=ttk.Button(ventanaInicio,text="Salir",style="MyButton.TButton",command=SalirJuego)
BotonSalir.place(x=25,y=230,width=250,height=35)

#Main
ventanaInicio.mainloop()
