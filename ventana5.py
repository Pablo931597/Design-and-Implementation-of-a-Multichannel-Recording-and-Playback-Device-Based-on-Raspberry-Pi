from tkinter import *
import tkinter
from tkinter import ttk
import ventana4
import Prueba
import threading
import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os

def parar():
    nuevo_valor = not stop.get()
    if nuevo_valor == True:
        pause.config(text='>')
    else:
        pause.config(text='||')
    stop.set(nuevo_valor)
    #ventana.destroy()
    #ventana2.mostrar_ventana()
    
def get_stop():
    return stop.get()

def get_finish():
    return finish.get()

def schedule_check(audio_thread):
    ventana5.after(1000, check_if_done, audio_thread)
    
def check_if_done(audio_thread):
    if not audio_thread.is_alive():
        ventana5.destroy()
        ventana4.mostrar_ventana()
    else:
        schedule_check(audio_thread)
    
def reproducir():
    global audio_thread
    audio_thread = threading.Thread(target=Prueba.reproducir, args=(ventana4.file,ventana4.btnCH,ventana4.colores))
    audio_thread.daemon = True 
    audio_thread.start()
    schedule_check(audio_thread)

def get_barra_volumen():
    return progress

def mostrar_ventana():
    global ventana5
    global stop
    global finish
    global pause
    global progress
    
    ventana5 = Toplevel()     
    ventana5.title("Reproduciendo")
    ventana5.geometry("800x480")
    
    reproducir()
    
    stop = tkinter.BooleanVar()
    stop.set(False)
    
    finish = tkinter.BooleanVar()
    finish.set(False)
    
    nombre_canal = [Label(ventana5) for _ in range(8)] 
    
    texto = [tkinter.Entry(ventana5, width=45) for _ in range(8)]
    
    progress = [tkinter.DoubleVar()for _ in range(8)]
    
    barra_volumen = [ttk.Progressbar(ventana5,variable=progress[l],maximum=100, orient="horizontal", length=200, mode="determinate")
                     for l in range(8)]

    def finished():
        finish.set(True)
    
    pause = tkinter.Button(ventana5,text ='||',width=84, height=3,font=("arial",12),relief="groove",bd=10,command=parar)
    pause.place(x=0,y=300)
    
    finito = tkinter.Button(ventana5,text ='finalizar',width=84, height=3,font=("arial",12),relief="groove",bd=10,command=finished)
    finito.place(x=0,y=390)
    
    colors = []
    
    for y in range(8):
        for n in range(9):
            if ventana4.btnCH[y].cget('background') == ventana4.colores[n]:
                colors.append(n)
            else:
                pass
    
    for i in range(8):
        for x in range(9):
            if x == 0:
                pass
            else:
                if colors[i] == x:
                    nombre_file = os.path.basename(ventana4.file[x-1])
                    texto[i].insert(0, nombre_file)
                else:
                    pass
    
    texto[0].place(x=90,y=55)
    texto[1].place(x=90,y=80)
    texto[2].place(x=90,y=105)
    texto[3].place(x=90,y=130)
    texto[4].place(x=90,y=155)
    texto[5].place(x=90,y=180)
    texto[6].place(x=90,y=205)
    texto[7].place(x=90,y=230)
    
    nombre_canal[0].config(text = "ch1:")
    nombre_canal[1].config(text = "ch2:")
    nombre_canal[2].config(text = "ch3:")
    nombre_canal[3].config(text = "ch4:")
    nombre_canal[4].config(text = "ch5:")
    nombre_canal[5].config(text = "ch6:")
    nombre_canal[6].config(text = "ch7:")
    nombre_canal[7].config(text = "ch8:")    
    
    nombre_canal[0].place(x=40,y=55)
    nombre_canal[1].place(x=40,y=80)
    nombre_canal[2].place(x=40,y=105)
    nombre_canal[3].place(x=40,y=130)
    nombre_canal[4].place(x=40,y=155)
    nombre_canal[5].place(x=40,y=180)
    nombre_canal[6].place(x=40,y=205)
    nombre_canal[7].place(x=40,y=230)
    
    style = ttk.Style()
    style.configure("TProgressbar", thickness=5)
    
    barra_volumen[0].place(x=470,y=63)
    barra_volumen[1].place(x=470,y=88)
    barra_volumen[2].place(x=470,y=113)
    barra_volumen[3].place(x=470,y=138)
    barra_volumen[4].place(x=470,y=164)
    barra_volumen[5].place(x=470,y=188)
    barra_volumen[6].place(x=470,y=213)
    barra_volumen[7].place(x=470,y=238)
    #ventana5.mainloop()

