import time
import tkinter as tk
from tkinter import ttk

ventanaInicio=tk.Tk()
ventanaInicio.title("Tic Tac Toe")
ventanaInicio.configure(bg='black')
ventanaInicio.geometry("300x400+618+232")

FondBoton=ttk.Style()
FondBoton.configure("MyButton.TButton",font=("Times",15))
global XO
XO=1

def JugarJ2():

    def BotonRegresar():
        BotonJugarCPU.place(x=25, y=150, width=250, height=35)
        BotonJugarJ2.place(x=25, y=190, width=250, height=35)
        BotonSalir.place(x=25, y=230, width=250, height=35)
        BotonRegresar.place_forget()
        Boton1.place_forget()
        Boton2.place_forget()
        Boton3.place_forget()
        Boton4.place_forget()
        Boton5.place_forget()
        Boton6.place_forget()
        Boton7.place_forget()
        Boton8.place_forget()
        Boton9.place_forget()
        Label1.place_forget()
        Label2.place_forget()
        Label3.place_forget()
        Label4.place_forget()
        Label5.place_forget()
        Label6.place_forget()
        Label7.place_forget()
        Label8.place_forget()
        Label9.place_forget()

    def ActionBoton(Numero):
        global XO
        if(Numero == 1):
            if(XO==1):
                Boton1.place_forget()
                Texto1.set("X")
                XO=2
            else:
                Boton1.place_forget()
                Texto1.set("O")
                XO=1
        if (Numero == 2):
            if (XO == 1):
                Boton2.place_forget()
                Texto2.set("X")
                XO = 2
            else:
                Boton2.place_forget()
                Texto2.set("O")
                XO = 1
        if (Numero == 3):
            if (XO == 1):
                Boton3.place_forget()
                Texto3.set("X")
                XO = 2
            else:
                Boton3.place_forget()
                Texto3.set("O")
                XO = 1
        if (Numero == 4):
            if (XO == 4):
                Boton2.place_forget()
                Texto4.set("X")
                XO = 2
            else:
                Boton4.place_forget()
                Texto4.set("O")
                XO = 1
        if (Numero == 5):
            if (XO == 1):
                Boton5.place_forget()
                Texto5.set("X")
                XO = 2
            else:
                Boton5.place_forget()
                Texto5.set("O")
                XO = 1
        if (Numero == 6):
            if (XO == 1):
                Boton6.place_forget()
                Texto6.set("X")
                XO = 2
            else:
                Boton6.place_forget()
                Texto6.set("O")
                XO = 1
        if (Numero == 7):
            if (XO == 1):
                Boton7.place_forget()
                Texto7.set("X")
                XO = 2
            else:
                Boton7.place_forget()
                Texto7.set("O")
                XO = 1
        if (Numero == 8):
            if (XO == 1):
                Boton8.place_forget()
                Texto8.set("X")
                XO = 2
            else:
                Boton8.place_forget()
                Texto8.set("O")
                XO = 1
        if (Numero == 9):
            if (XO == 1):
                Boton9.place_forget()
                Texto9.set("X")
                XO = 2
            else:
                Boton9.place_forget()
                Texto9.set("O")
                XO = 1

    time.sleep(0.1)
    BotonSalir.place_forget()
    BotonJugarCPU.place_forget()
    BotonJugarJ2.place_forget()

    #Labels de la Fila 1
    Texto1=tk.StringVar()
    Texto1.set("")
    Label1 = tk.Label(ventanaInicio, textvariable=Texto1, fg="red", bg="black")
    Label1.place(x=20, y=10, width=80, height=80)
    Texto2 = tk.StringVar()
    Texto2.set("")
    Label2 = tk.Label(ventanaInicio, textvariable=Texto2, fg="red", bg="black")
    Label2.place(x=110, y=10, width=80, height=80)
    Texto3 = tk.StringVar()
    Texto3.set("")
    Label3 = tk.Label(ventanaInicio, textvariable=Texto3, fg="red", bg="black")
    Label3.place(x=200, y=10, width=80, height=80)
    #Labels de la Fila 2
    Texto4 = tk.StringVar()
    Texto4.set("")
    Label4 = tk.Label(ventanaInicio, textvariable=Texto4, fg="red", bg="black")
    Label4.place(x=20, y=100, width=80, height=80)
    Texto5 = tk.StringVar()
    Texto5.set("")
    Label5 = tk.Label(ventanaInicio, textvariable=Texto5, fg="red", bg="black")
    Label5.place(x=110, y=100, width=80, height=80)
    Texto6 = tk.StringVar()
    Texto6.set("")
    Label6 = tk.Label(ventanaInicio, textvariable=Texto6, fg="red", bg="black")
    Label6.place(x=200, y=100, width=80, height=80)
    #Labels de la Fila 3
    Texto7 = tk.StringVar()
    Texto7.set("")
    Label7 = tk.Label(ventanaInicio, textvariable=Texto7, fg="red", bg="black")
    Label7.place(x=20, y=190, width=80, height=80)
    Texto8 = tk.StringVar()
    Texto8.set("")
    Label8 = tk.Label(ventanaInicio, textvariable=Texto8, fg="red", bg="black")
    Label8.place(x=110, y=190, width=80, height=80)
    Texto9 = tk.StringVar()
    Texto9.set("")
    Label9 = tk.Label(ventanaInicio, textvariable=Texto9, fg="red", bg="black")
    Label9.place(x=200, y=190, width=80, height=80)

    BotonRegresar = ttk.Button(ventanaInicio, text="Regresar", style="MyButton.TButton", command=BotonRegresar)
    BotonRegresar.place(x=190, y=355, width=100, height=35)
    #Fila 1 de botones
    Boton1 = ttk.Button(ventanaInicio, text="1", style="MyButton.TButton",command=lambda:ActionBoton(1))
    Boton1.place(x=20, y=10, width=80, height=80)
    Boton2 = ttk.Button(ventanaInicio, text="2", style="MyButton.TButton",command=lambda:ActionBoton(2))
    Boton2.place(x=110, y=10, width=80, height=80)
    Boton3 = ttk.Button(ventanaInicio, text="3", style="MyButton.TButton",command=lambda:ActionBoton(3))
    Boton3.place(x=200, y=10, width=80, height=80)
    #Fila 2 de botones
    Boton4 = ttk.Button(ventanaInicio, text="4", style="MyButton.TButton",command=lambda:ActionBoton(4))
    Boton4.place(x=20, y=100, width=80, height=80)
    Boton5 = ttk.Button(ventanaInicio, text="5", style="MyButton.TButton",command=lambda:ActionBoton(5))
    Boton5.place(x=110, y=100, width=80, height=80)
    Boton6 = ttk.Button(ventanaInicio, text="6", style="MyButton.TButton",command=lambda:ActionBoton(6))
    Boton6.place(x=200, y=100, width=80, height=80)
    #Fila 3 de botones
    Boton7 = ttk.Button(ventanaInicio, text="7", style="MyButton.TButton",command=lambda:ActionBoton(7))
    Boton7.place(x=20, y=190, width=80, height=80)
    Boton8 = ttk.Button(ventanaInicio, text="8", style="MyButton.TButton",command=lambda:ActionBoton(8))
    Boton8.place(x=110, y=190, width=80, height=80)
    Boton9 = ttk.Button(ventanaInicio, text="9", style="MyButton.TButton",command=lambda:ActionBoton(9))
    Boton9.place(x=200, y=190, width=80, height=80)



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

def SalirJuego():
    ventanaInicio.destroy()
#def ventanaJugar():
#    if BotonSalir.winfo_ismapped():
#        BotonSalir.place_forget()
#    else:
#        BotonSalir.place(x=25, y=190, width=250, height=35)
#LogoJuego=tkinter.Label(ventanaInicio,image=tkinter.PhotoImage(file="LogoNombre.jpg"))
#LogoJuego.pack()

BotonJugarCPU=ttk.Button(ventanaInicio,text="J1vs CPU",style="MyButton.TButton",command=JugarCPU)
BotonJugarCPU.place(x=25,y=150,width=250,height=35)

BotonJugarJ2=ttk.Button(ventanaInicio,text="J1 vs J2",style="MyButton.TButton",command=JugarJ2)
BotonJugarJ2.place(x=25,y=190,width=250,height=35)

BotonSalir=ttk.Button(ventanaInicio,text="Salir",style="MyButton.TButton",command=SalirJuego)
BotonSalir.place(x=25,y=230,width=250,height=35)

ventanaInicio.mainloop()