from tkinter import *
from mis_librerias import Centrar_Ventana

def main():
    centrar = Centrar_Ventana
    raiz = Tk()
    raiz.title("Informacion del creador")
    raiz.geometry(centrar.centrar_ventana(380,200,raiz))
    
    frame = Frame(raiz)
    frame.config(bg="#%02x%02x%02x" % (84,146,203))
    frame.pack(fill="both",expand=True)
    
    label = Text(frame)
    label.insert(INSERT,"\n \n \n Creado por: Lazaro Altedill Hernandez \n tel:55560720 \n correo: lazaroah02@gmail.com")
    label.config(width=40,height=10,font=("Courier",11,"italic"),state=DISABLED,bg="#%02x%02x%02x" % (84,146,203))
    label.place(x=10,y=10)
    raiz.mainloop()
