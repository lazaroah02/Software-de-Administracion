from tkinter import *
from mis_librerias import Centrar_Ventana,RGB
def main(usuario,tipo):
    tipo_raiz = tipo #recibimos el tipo de raiz segun de q ventana llamemos esta, desde administrador con toplevel para q no den conflictos las imagenes y desde login Tk
    rgb = RGB
    centrar = Centrar_Ventana
    nombre_usuario = usuario
    raiz = tipo_raiz
    raiz.title("Tecnico -- Sesion de: " + nombre_usuario)
    raiz.geometry(centrar.centrar_ventana(500,300,raiz))
    raiz.resizable()
    
    frame = Frame(raiz)
    frame.config(bg=rgb.RGB((84,146,203)))
    frame.pack(fill="both",expand=True)
    
    label_encabezado = Label(frame,text="Bienvenido " + nombre_usuario)
    label_encabezado.config(font=("Courier",16,"italic"),width=40,bg=rgb.RGB((84,146,203)))
    label_encabezado.place(x=0,y=10)
    
    imag1 = PhotoImage(file="Imagenes/apoyo-tecnico.png")
    boton_gestion_equipos = Button(frame,image=imag1)
    boton_gestion_equipos.config(width=100, height=100)
    boton_gestion_equipos.place(x=50,y=100)
    
    label_gestion_equipo = Label(frame,text="Gestion de Equipos")
    label_gestion_equipo.config(bg=rgb.RGB((84,146,203)))
    label_gestion_equipo.place(x=50,y=205)
    
    imag2 = PhotoImage(file="Imagenes/grafica.png")
    boton_grafica_estatus = Button(frame,image=imag2)
    boton_grafica_estatus.config(width=100, height=100)
    boton_grafica_estatus.place(x=200,y=100)
    
    label_grafica_estatus = Label(frame,text="Grafica de Estatus")
    label_grafica_estatus.config(bg=rgb.RGB((84,146,203)))
    label_grafica_estatus.place(x=197,y=205)
    
    imag3 = PhotoImage(file="Imagenes/grafica.png")
    boton_grafica_marcas = Button(frame,image=imag3)
    boton_grafica_marcas.config(width=100, height=100)
    boton_grafica_marcas.place(x=350,y=100)
    
    label_grafica_marcas = Label(frame,text="Grafica de marcas")
    label_grafica_marcas.config(bg=rgb.RGB((84,146,203)))
    label_grafica_marcas.place(x=350,y=205)
    
    raiz.mainloop()
