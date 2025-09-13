from tkinter import *
import tkinter
from tkinter import ttk
import ventana1
from tkinter import filedialog
import Prueba
import os
import numpy as np
import ventana5
import matplotlib.pyplot as plt
import ventana1

def regresar():
    ventana4.destroy()
    ventana1.get_raiz().iconify()
    ventana1.get_raiz().deiconify()
    
def select_file():
    valor = 0
    for j in range(8):
        if file[j] == '':
            valor = j
            break
        elif not file[7] == '':
            valor = 7
            break
    
    file_path = tkinter.filedialog.askopenfilename(initialdir='/home/pi3/Desktop/TFG/Grabaciones',title='Files',filetypes=[('archivos wav','*.wav')])
    string_var[valor].set(file_path)
    file_name = os.path.basename(file_path)
    campo_texto[valor].delete(0, tkinter.END)
    campo_texto[valor].insert(0, file_name)
    file[valor] = file_path
    
    if file[0] == '':
        btnB['state']='disable'
    else:
        btnB.config(state=tkinter.NORMAL)
        cambiar_color_circulo(circulo[valor])
        btnB['state']='normal'
    
    if not file[7] == '':
        btn2['state']='disable'
    
    
def actualizar_boton():
    x = 0
    blanco = 0
    for i in range (8):
        #if string_var[i].get().strip():
            #x = x + 1
        if btnCH[i].cget("background") == colores[0]:
            blanco = blanco + 1
        else:
            pass
    if blanco == 8:
        btn18['state']='disable'
    else:       
        btn18.config(state=tkinter.NORMAL)
        
#def file_list():
    #array = []
    #for n in range(8):
        #for i in range(1,9):
            #if colores[i] == canvas.itemcget(circulo[n],"fill"):
                #array.append(i)
            #else:
                #pass
            
    #for m in range(len(array)):
        #file.append(string_var[m].get())
    
    #print(file)
    
def cambiar_color_circulo(circulo):
    
    valor = 0
    for i in range(9):
        if i == 0:
            pass
        elif valores[i] == False:
            valores[i] = True
            valor = i
            break
        
    #canvas.itemcget(circulo[i],"fill") != colores[x]: 
    
    canvas.itemconfig(circulo, fill= colores[valor])
    
def cambiar_a_blanco(circulo):
    color = canvas.itemcget(circulo,"fill")
    if color == colores[0]:
        valores[0] == True
    else:
        valor = 0
        for x in range(9):
            if color == colores[x]:
                valor = x
                break
            else:
                pass
                
        valores[valor] = False
            
    canvas.itemconfig(circulo, fill=colores[0])        
                
def borrar():
    valor = 0
    for i in range(8):
        if file[i] == '':
            valor = i
            break
        elif not file[7] == '':
            valor = 8
    
    file[valor-1] = ''
    campo_texto[valor-1].delete(0, tkinter.END)
        
    for i in range(8):
        if canvas.itemcget(circulo[i],"fill") == btnCH[i].cget("background"):
            btnCH[i].config(bg = colores[0])
                
    cambiar_a_blanco(circulo[valor-1])
    string_var[valor-1].set('')
    
    if file[0] == '':
        btnB['state']='disable'
    #btn.config(state=tkinter.NORMAL)
    actualizar_boton()
    btn2['state']='normal'
    
def reproducir():
    #file_list()
    ventana4.withdraw()
    ventana5.mostrar_ventana()
    #Prueba.reproducir(file,btnCH,colores)

def file():
    return file

def btnCH():
    return btnCH

def colores():
    return colores

def select_channel(btnCH):
    valor = 0
    color = btnCH.cget("background")
    nuevo = 0
    no_true = 0
    if color == colores[8]:
        nuevo = 0
    else:
        for x in range(9):
            if color == colores[x]:
                valor = x
            else:
                pass
            
        for i in range(valor+1, 9):
            if valores[i] == True:
                nuevo = i
                no_true = 1
                break
            else:
                pass
                
    if no_true == 1:
        btnCH.config(bg = colores[nuevo])
    else:
        btnCH.config(bg = colores[0])
    
    actualizar_boton()

def mostrar_ventana():
    global ventana4
    global string_var
    global btn18
    global campo_texto
    global btnB
    global colores
    global circulo
    global canvas
    global valores
    global btnCH
    global file
    global btn2
    
    ventana4 = Toplevel()
    
    ventana4.title("Reproductor")
    ventana4.geometry("800x480")

    string_var = [tkinter.StringVar() for _ in range(8)]
    campo_texto = [tkinter.Entry(ventana4, width=35) for _ in range(8)]
    btnB = tkinter.Button(ventana4)
    btnCH =[Button(ventana4, font=("arial",18),bg="white",
                 fg="black",padx=1,pady=1,relief="groove",bd=5) for _ in range(8)]
    canvas = tkinter.Canvas(ventana4, width=50, height=500)
    canvas.pack()
    x0, y0 = 20, 20
    x1, y1 = 40, 40
    colores = ["white","green","red","blue","purple","orange","yellow","lightblue","lightgreen"]
    circulo = [canvas.create_oval(x0, y0, x1, y1, fill=colores[0], outline="black")for _ in range(8)]
    valores = [True,False,False,False,False,False,False,False,False]
    file = ['','','','','','','','']
    
    label1 = Label(ventana4,text="Seleccionar salidas")
    label1.place(x=500,y=5)
    
    label2 = Label(ventana4,text="Seleccionar archivos a reproducir")
    label2.place(x=115,y=5)
 
    btn = Button(ventana4,text="Back",command=regresar)
    btn.place(x=10,y=10) 
    
    btn2 = Button(ventana4,text="Select file",command=lambda:select_file())
    btn2.place(x=140, y=25)
    
    btnB.config(text="Borrar",command=lambda:borrar())
    btnB.config(state=tkinter.DISABLED)
    btnB.place(x=235, y=25)
        
    campo_texto[0].place(x=90,y=55)
    
    canvas.move(circulo[0],2,35)
    
    campo_texto[1].place(x=90,y=110)    
    
    canvas.move(circulo[1],2,92)
     
    campo_texto[2].place(x=90,y=165)
    
    canvas.move(circulo[2],2,147)
    
    campo_texto[3].place(x=90,y=220)
    
    canvas.move(circulo[3],2,202)

    campo_texto[4].place(x=90,y=275)
    
    canvas.move(circulo[4],2,260)
    
    campo_texto[5].place(x=90,y=330)
    
    canvas.move(circulo[5],2,312)
    
    campo_texto[6].place(x=90,y=385)
    
    canvas.move(circulo[6],2,367)
    
    campo_texto[7].place(x=90,y=440)    
    
    canvas.move(circulo[7],2,422)
    
    btnCH[0].config(text ='Ch-1',command=lambda:select_channel(btnCH[0]))
    btnCH[0].place(x=520,y=50)
    
    btnCH[1].config(text ='Ch-2',command=lambda:select_channel(btnCH[1]))
    btnCH[1].place(x=520,y=100)
    
    btnCH[2].config(text ='Ch-3',command=lambda:select_channel(btnCH[2]))
    btnCH[2].place(x=520,y=150)
    
    btnCH[3].config(text ='Ch-4',command=lambda:select_channel(btnCH[3]))
    btnCH[3].place(x=520,y=200)
    
    btnCH[4].config(text ='Ch-5',command=lambda:select_channel(btnCH[4]))
    btnCH[4].place(x=520,y=250)
    
    btnCH[5].config(text ='Ch-6',command=lambda:select_channel(btnCH[5]))
    btnCH[5].place(x=520,y=300)
    
    btnCH[6].config(text ='Ch-7',command=lambda:select_channel(btnCH[6]))
    btnCH[6].place(x=520,y=350)
    
    btnCH[7].config(text ='Ch-8',command=lambda:select_channel(btnCH[7]))
    btnCH[7].place(x=520,y=400)
    

    btn18 = Button(ventana4,text="Reproducir",font=("arial",18),bg="lightgray",
                 fg="black",padx=5,pady=20,relief="groove",bd=5,command=reproducir)
    btn18.place(x=630, y=190)
    btn18.config(state=tkinter.DISABLED)
    
    #ventana4.mainloop()
    