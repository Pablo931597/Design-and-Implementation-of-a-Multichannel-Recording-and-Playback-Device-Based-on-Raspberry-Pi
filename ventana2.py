from tkinter import *
import tkinter
from tkinter import ttk
import ventana1
import ventana3
import Grabador
import threading

def regresar():
    ventana2.destroy()
    ventana1.get_raiz().iconify()
    ventana1.get_raiz().deiconify()

def select_channel(btnCH,posicion):
    if yesno[posicion] == True:
        yesno[posicion] = False
    else:
        yesno[posicion] = True
    
    if yesno[posicion] == True:
        btnCH.config(bg = 'red')
    else:
        btnCH.config(bg = 'white')

    actualizar_boton()


def grabar():
    ventana2.destroy()
    ventana3.mostrar_ventana()

def get_yesno():
    return yesno
    
def actualizar_boton():
    x = 0
    for v in range(8):
        if yesno[v] == True:
            x = x+1
        else:
            x = x
            
    if x == 0:
        rec['state']='disable'
    else:
        rec.config(state=tkinter.NORMAL)
    
def mostrar_ventana():
    global ventana2
    global btnCH
    global yesno
    global rec
    
    ventana2 = Toplevel()
    ventana2.title("Record")
    ventana2.geometry("800x480")
    #ventana2.config(width=800, height=480)
    #ventana2.config(width="800",height="480",bg="white")
    yesno = [False,False,False,False,False,False,False,False]
    btnCH =[Button(ventana2, font=("arial",18),bg="white",
                 fg="black",padx=1,pady=1,relief="groove",bd=5) for _ in range(8)]
    
    label = Label(ventana2,text="Seleccionar entradas")
    label.place(x=100,y=20)
    
    btn = Button(ventana2,text="Back",command=regresar)
    btn.place(x=10,y=10)
    
    btnCH[0].config(text ='Ch-1',command=lambda:select_channel(btnCH[0],0))
    btnCH[0].place(x=130,y=50)
    
    btnCH[1].config(text ='Ch-2',command=lambda:select_channel(btnCH[1],1))
    btnCH[1].place(x=130,y=100)
    
    btnCH[2].config(text ='Ch-3',command=lambda:select_channel(btnCH[2],2))
    btnCH[2].place(x=130,y=150)
    
    btnCH[3].config(text ='Ch-4',command=lambda:select_channel(btnCH[3],3))
    btnCH[3].place(x=130,y=200)
    
    btnCH[4].config(text ='Ch-5',command=lambda:select_channel(btnCH[4],4))
    btnCH[4].place(x=130,y=250)
    
    btnCH[5].config(text ='Ch-6',command=lambda:select_channel(btnCH[5],5))
    btnCH[5].place(x=130,y=300)
    
    btnCH[6].config(text ='Ch-7',command=lambda:select_channel(btnCH[6],6))
    btnCH[6].place(x=130,y=350)
    
    btnCH[7].config(text ='Ch-8',command=lambda:select_channel(btnCH[7],7))
    btnCH[7].place(x=130,y=400)
    
    rec = Button(ventana2,text ='REC',width=15, height=7,font=("arial",12),relief="groove",bd=10,command=grabar)
    rec.place(x=330,y=150)
    rec.config(state=tkinter.DISABLED)
    
    #ventana2.mainloop()
