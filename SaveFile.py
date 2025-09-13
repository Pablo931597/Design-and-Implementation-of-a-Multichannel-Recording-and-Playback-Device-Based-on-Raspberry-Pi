from tkinter import *
import tkinter
from tkinter import ttk
import ventana2

def si():
    guardar.set(True)
    savefile.destroy()
    #ventana2.mostrar_ventana()
def no():
    guardar.set(False)
    savefile.destroy()
    #ventana2.mostrar_ventana()

def guardarwav():
    return guardar.get()

def mostrar_ventana(nombre):
    global savefile
    global guardar
    
    savefile = Toplevel()
    savefile.title("Guardar archivo")
    savefile.geometry("400x240")
 
    guardar = tkinter.BooleanVar()
    guardar.set(False)
    texto = tkinter.StringVar()
    
    campo_texto = tkinter.Entry(savefile)
    campo_texto.insert(0, nombre)
    campo_texto.config(width=37)
    campo_texto.place(x=60,y=90)
    
    label = tkinter.Label(savefile, text="Quiere guardar el archivo:",font=("arial", 11),)
    label.place(x=120,y=50)
    
    btn1 = Button(savefile,text="Si",command=si)
    btn1.place(x=150,y=130)
    btn2 = Button(savefile,text="No",command=no)
    btn2.place(x=210,y=130)
    savefile.wait_window()
    #ventana.mainloop()
    