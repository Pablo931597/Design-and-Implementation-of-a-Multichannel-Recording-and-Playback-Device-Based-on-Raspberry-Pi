from tkinter import *
import tkinter
from tkinter import ttk
import ventana2
import ventana3
import ventana4
from PIL import Image, ImageTk

def go2():
    ventana.withdraw()
    ventana2.mostrar_ventana()

def go4():
    ventana.withdraw()
    ventana4.mostrar_ventana()

def get_raiz():
    return ventana


def mostrar_ventana():
    global ventana
    #global raiz
    
    ventana = Tk()
    ventana.title("Menu Principal")
    ventana.geometry("800x480")
    ventana.config(bg="white")
    #ventana = Frame()
    #ventana.pack(fill="both",expand="True")
    #ventana.config(width="800",height="480",bg="white")
    
    image_path = "/home/pi3/Desktop/TFG/Interfaz/wave.jpg"
    imagen = Image.open(image_path)
    photo = ImageTk.PhotoImage(imagen)
    tkinter.Label(ventana, image= photo).place(x=0,y=80)
    #canvas = tkinter.Canvas(ventana, width=image.width, height=image.height)
    #canvas.pack()
    #x = 0
    #y = 80
    #canvas.create_image(x, y, anchor=tkinter.NW, image=photo)
    #canvas.image = photo
    
    texto = tkinter.StringVar()
    texto.set("Grabador reproductor: Samplerate = 48000Hz y Format = 24 bits ")
    label = tkinter.Label(ventana, textvariable=texto,bg="white",fg="purple",font=("arial", 18),)
    label.place(x=60,y=35)
    
    #canvas.config(bg="white")

    btn1 = Button(ventana,text="REC", width=10, height=5,font=("arial",18),bg="lightgray",
                 fg="purple",relief="groove",bd=10,command=go2)
    btn1.place(x=190,y=120)

    btn3 = Button(ventana,text="PLAY", width=10, height=5, font=("arial",18),bg="lightgray",
                 fg="purple",relief="groove",bd=10,command=go4)
    btn3.place(x=440,y=120)
    
    ventana.mainloop()
