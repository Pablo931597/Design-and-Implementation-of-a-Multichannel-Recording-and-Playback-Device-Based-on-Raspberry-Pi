from tkinter import *
import tkinter
from tkinter import ttk
import threading
import Grabador
import ventana2
import ventana1
import time

def act_cron():
    global inicio
    global duracion
      
    if duracion == 0:
        inicio = time.time()
    else:
        inicio = time.time() - duracion
    
    ventana3.after(500,actualizar_cron)        
    
def actualizar_cron():
    global inicio
    global duracion
    
    duracion = time.time() - inicio
    horas = int(duracion//60//60)
    minutos = int(duracion//60%60)
    segundos = int(duracion%60)
    
    tiempo.set(f"{horas:02d}:{minutos:02d}:{segundos:02d}")
    tarea = ventana3.after(500,actualizar_cron)
    
def get_barra_volumen():
    return progress    
    
def regresar():
    ventana3.destroy()
    ventana2.mostrar_ventana()

def grabar():
    #global audio_thread
    audio_thread = threading.Thread(target=Grabador.iniciar_grabacion, args = (ventana2.get_yesno())) 
    audio_thread.daemon = True
    audio_thread.start()
    schedule_check(audio_thread)
    
def parar():
    print('Grabacion finalizada.')
    stop.set(True)
    #ventana.destroy()
    #ventana2.mostrar_ventana()

def get_stop():
    return stop.get()

def schedule_check(audio_thread):
    ventana3.after(1000, check_if_done, audio_thread)
    
def check_if_done(audio_thread):
    if not audio_thread.is_alive():
        ventana3.destroy()
        ventana2.mostrar_ventana()
    else:
        schedule_check(audio_thread)
    
def mostrar_ventana():
    
    global ventana3
    global stop
    global detener_hilo
    global segudos,minutos,horas,inicio,duracion,tarea,tiempo
    global cronometro
    global progress
    
    segundos = 0
    minutos = 0
    horas = 0
    inicio = 0
    duracion = 0
    tarea = None
    
    tiempo = tkinter.StringVar()
    tiempo.set(f"00:00:00")
    
    ventana3 = Toplevel()
    ventana3.title("Parar grabacion")
    ventana3.geometry("800x480")
    
    stop = tkinter.BooleanVar()
    stop.set(False)
    
    grabar()
    act_cron()
    
    STOP = Button(ventana3,text ='STOP',width=84, height=8,font=("arial",12),relief="groove",bd=10,command=parar)
    STOP.place(x=0,y=300)
    
    cronometro = tkinter.Label(ventana3, textvariable=tiempo, font=("Helvetica", 48),bg="black",fg="darkgreen")
    cronometro.pack(pady=30)
    
    nombre_canal = [Label(ventana3) for _ in range(8)]
    
    progress = [tkinter.DoubleVar()for _ in range(8)]
    barra_volumen = [ttk.Progressbar(ventana3,variable=progress[l],maximum=100, orient="vertical", length=150, mode="determinate")
                     for l in range(8)]
    style = ttk.Style()
    style.configure("TProgressbar", thickness=5)
    
    nombre_canal[0].config(text = "ch1")
    nombre_canal[1].config(text = "ch2")
    nombre_canal[2].config(text = "ch3")
    nombre_canal[3].config(text = "ch4")
    nombre_canal[4].config(text = "ch5")
    nombre_canal[5].config(text = "ch6")
    nombre_canal[6].config(text = "ch7")
    nombre_canal[7].config(text = "ch8")
    
    nombre_canal[0].place(x=280,y=265)
    nombre_canal[1].place(x=310,y=265)
    nombre_canal[2].place(x=340,y=265)
    nombre_canal[3].place(x=370,y=265)
    nombre_canal[4].place(x=400,y=265)
    nombre_canal[5].place(x=430,y=265)
    nombre_canal[6].place(x=460,y=265)
    nombre_canal[7].place(x=490,y=265)
    
    barra_volumen[0].place(x=290,y=110)
    barra_volumen[1].place(x=320,y=110)
    barra_volumen[2].place(x=350,y=110)
    barra_volumen[3].place(x=380,y=110)
    barra_volumen[4].place(x=410,y=110)
    barra_volumen[5].place(x=440,y=110)
    barra_volumen[6].place(x=470,y=110)
    barra_volumen[7].place(x=500,y=110)
    
    #ventana.mainloop()
    
