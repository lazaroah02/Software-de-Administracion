from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox
from mis_librerias import Connection_BD,RGB
import os,sys

def main(a):
    rgb = RGB
    usuario = a
    raiz = Toplevel()
    raiz.title("Registrar nuevo cliente -- Sesion de: " + usuario)
    raiz.resizable(0,0)
    
    frame = Frame(raiz)
    frame.config(width =400,height=400,bg=rgb.RGB((84,146,203)))
    frame.pack(fill = "both",expand = True)
    
    label_encabezado = Label(frame,text = "Registrar nuevo cliente")
    label_encabezado.config(width = 20,height=5,font=18,bg=rgb.RGB((84,146,203)))
    label_encabezado.place(x = 80,y = 10)
    
    label_nombre = Label(frame,text = "Nombre Completo")
    label_nombre.config(bg=rgb.RGB((84,146,203)))
    label_nombre.place(x = 10,y =130 )
    
    entry_nombre = Entry(frame)
    entry_nombre.config(width =25)
    entry_nombre.place(x = 10,y =160)
    
    label_email = Label(frame,text = "Email")
    label_email.config(bg=rgb.RGB((84,146,203)))
    label_email.place(x = 10,y =200 )
    
    entry_email = Entry(frame)
    entry_email.config(width =25)
    entry_email.place(x = 10,y =230)
    
    label_telefono = Label(frame,text = "Telefono")
    label_telefono.config(bg=rgb.RGB((84,146,203)))
    label_telefono.place(x = 10,y =270 )
    
    entry_telefono = Entry(frame)
    entry_telefono.config(width =25)
    entry_telefono.place(x = 10,y =300)
    
    imagen = PhotoImage(file="Imagenes/add.png")
    boton = Button(frame,image=imagen)
    boton.config(width=100,height=100)
    boton.place(x =230,y =200)
    #metodo para el codigo del boton agregar
    def Codigo_boton():
        
        if entry_nombre.get() == "" :
            entry_nombre.config(bg ="red")
            MessageBox.showinfo("Error","Debes ingresar el nombre")
            entry_nombre.config(bg ="white")
        elif entry_email.get() == "" :
            entry_email.config(bg ="red")
            MessageBox.showinfo("Error","Debes ingresar el email")
            entry_email.config(bg ="white")
        elif entry_telefono.get() == "" :
            entry_telefono.config(bg ="red")
            MessageBox.showinfo("Error","Debes ingresar el telefono")
            entry_telefono.config(bg ="white")
            
        else:
             connect = Connection_BD #instancio para establecer coneccion
             try:
                 connection = connect.connection()
                 cursor = connection.cursor()
                 nombre = entry_nombre.get()
                 email = entry_email.get()
                 telefono = entry_telefono.get()
                 
                 sql = "INSERT INTO clientes VALUES(NULL,'{}','{}','{}','{}')".format(
                     nombre,
                     email.replace(" ",""),
                     telefono.replace(" ",""),
                     usuario
                 )
                 cursor.execute(sql)
                 connection.commit()
                 MessageBox.showinfo("","Cliente agragado exitosamente")
                 entry_nombre.delete(0,"end")
                 entry_email.delete(0,"end")
                 entry_telefono.delete(0,"end")
                
                 
             except:
                 print("Error de conexion")   
            
    boton.config(command = Codigo_boton)
    raiz.mainloop()