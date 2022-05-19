from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox
from mis_librerias import Connection_BD,RGB
import os,sys

def main(a):
    rgb = RGB
    usuario = a
    raiz = Toplevel()
    raiz.title("Registrar nuevo usuario -- Sesion de: " + usuario)
    raiz.resizable(0,0)
    
    frame = Frame(raiz)
    frame.config(width =500,height=500,bg=rgb.RGB((84,146,203)))
    frame.pack(fill = "both",expand = True)
    
    label_encabezado = Label(frame,text = "Registrar nuevo usuario")
    label_encabezado.config(width = 20,height=5,font=18,bg=rgb.RGB((84,146,203)))
    label_encabezado.place(x = 130,y = 10)
    
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
    
    label_permisos = Label(frame,text = "Permisos de:")
    label_permisos.config(bg=rgb.RGB((84,146,203)))
    label_permisos.place(x = 10,y =350 )
    
    box_permisos = ttk.Combobox(frame,state ="readonly",values =["Administrador","Capturista","Tecnico"])
    box_permisos.set("Tecnico")
    box_permisos.place(x = 10,y =380)
    
    label_username = Label(frame,text = "Username")
    label_username.config(bg=rgb.RGB((84,146,203)))
    label_username.place(x = 300,y =130)
    
    entry_username = Entry(frame)
    entry_username.config(width =25)
    entry_username.place(x = 300,y =160)
    
    label_pass = Label(frame,text = "Password")
    label_pass.config(bg=rgb.RGB((84,146,203)))
    label_pass.place(x = 300,y =200)
    
    entry_pass = Entry(frame)
    entry_pass.config(width =25)
    entry_pass.place(x = 300,y =230)
    
    imagen = PhotoImage(file="Imagenes/add.png")
    boton = Button(frame,image=imagen)
    boton.config(width=100,height=100)
    boton.place(x =330,y =300)
    #metodo para el codigo del boton agregar
    def Codigo_boton():
        
        if entry_nombre.get() == "" :
            entry_nombre.config(bg ="red")
            MessageBox.showinfo("Error","Debes ingresar tu nombre")
            entry_nombre.config(bg ="white")
        elif entry_email.get() == "":
            entry_email.config(bg ="red")
            MessageBox.showinfo("Error","Debes ingresar tu email")
            entry_email.config(bg ="white")
        elif entry_telefono.get() == "":
            entry_telefono.config(bg ="red")
            MessageBox.showinfo("Error","Debes ingresar tu telefono")
            entry_telefono.config(bg ="white")
        elif entry_username.get() == "":
            entry_username.config(bg ="red")
            MessageBox.showinfo("Error","Debes ingresar un username")
            entry_username.config(bg ="white")
        elif  entry_pass.get() == "":
            entry_pass.config(bg ="red")
            MessageBox.showinfo("Error","Debes ingresar un password")
            entry_pass.config(bg ="white")    
        else:
             connect = Connection_BD #instancio para establecer coneccion
             try:
                 connection = connect.connection()
                 cursor = connection.cursor()
                 
                 user = entry_username.get()
                 pas = entry_pass.get()
                 box = box_permisos.get()
                 mail = entry_email.get()
                 name = entry_nombre.get()
                 tel = entry_telefono.get()
                 
                 sql = "INSERT INTO usuarios VALUES(NULL,'{}','{}','{}','{}','{}','{}','{}','{}')".format(
                     user.replace(" ",""),
                     pas.replace(" ",""),
                     box,
                     "Activo",
                     mail.replace(" ",""),
                     name,
                     tel.replace(" ",""),
                     usuario
                 )
                 cursor.execute(sql)
                 connection.commit()
                 MessageBox.showinfo("","Usuario agragado exitosamente")
                 
                 box_permisos.set("Tecnico")
                 entry_nombre.delete(0,"end")
                 entry_username.delete(0,"end")
                 entry_pass.delete(0,"end")
                 entry_email.delete(0,"end")     
                 entry_telefono.delete(0,"end")
                
                 
             except:
                 print("Error de conexion")   
            
    boton.config(command = Codigo_boton)
    raiz.mainloop()
