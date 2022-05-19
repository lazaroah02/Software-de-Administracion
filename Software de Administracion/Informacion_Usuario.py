from tkinter import *
from pymysql import NULL
from mis_librerias import Centrar_Ventana,Connection_BD,RGB
from tkinter import ttk,messagebox
conect = Connection_BD
connection = conect.connection()
usuario =[]
id_usuario = 0
def main():
    rgb = RGB
    centrar = Centrar_Ventana
    raiz = Tk()
    raiz.title("Informacion del usuario: " + usuario[6])
    raiz.geometry("400x400")
    raiz.resizable(0,0)
    
    frame = Frame(raiz)
    frame.config(bg=rgb.RGB((84,146,203)))
    frame.pack(fill="both",expand = True)
    
    label_nombre = Label(frame,text="Nombre")
    label_nombre.config(bg=rgb.RGB((84,146,203)))
    label_nombre.grid(row=0,column=0,padx=0,pady=10)
    
    entry_nombre = Entry(frame)
    entry_nombre.config(width=30)
    entry_nombre.insert(INSERT,usuario[6])
    entry_nombre.grid(row=0,column=1,padx=0,pady=10)
    
    label_email = Label(frame,text="Email")
    label_email.config(bg=rgb.RGB((84,146,203)))
    label_email.grid(row=1,column=0,padx=0,pady=0)
    
    entry_email = Entry(frame)
    entry_email.config(width=30)
    entry_email.insert(INSERT,usuario[5])
    entry_email.grid(row=1,column=1,padx=10,pady=10)
    
    label_telefono = Label(frame,text="Telefono")
    label_telefono.config(bg=rgb.RGB((84,146,203)))
    label_telefono.grid(row=2,column=0,padx=0,pady=10)
    
    entry_telefono = Entry(frame)
    entry_telefono.config(width=30)
    entry_telefono.insert(INSERT,usuario[7])
    entry_telefono.grid(row=2,column=1,padx=10,pady=10)
    
    label_permisos = Label(frame,text="Permisos")
    label_permisos.config(bg=rgb.RGB((84,146,203)))
    label_permisos.grid(row=3,column=0,padx=0,pady=10)
    
    box_permisos = ttk.Combobox(frame,state="readonly",value=["Administrador","Tecnico","Capturista"])
    box_permisos.set(usuario[3])
    box_permisos.config(width=27)
    box_permisos.grid(row=3,column=1,padx=10,pady=10)
    
    label_username = Label(frame,text="Username")
    label_username.config(bg=rgb.RGB((84,146,203)))
    label_username.grid(row=4,column=0,padx=10,pady=10)
    
    entry_username = Entry(frame)
    entry_username.config(width=30)
    entry_username.insert(INSERT,usuario[1])
    entry_username.grid(row=4,column=1,padx=10,pady=10)
    
    label_estatus = Label(frame,text="Estatus")
    label_estatus.config(bg=rgb.RGB((84,146,203)))
    label_estatus.grid(row=5,column=0,padx=0,pady=10)
    
    box_estatus = ttk.Combobox(frame,state="readonly",values=["Activo","Inactivo"])
    box_estatus.config(width = 27)
    box_estatus.set(usuario[4])
    box_estatus.grid(row=5,column=1,padx=10,pady=10)
    
    
    def boton_actualizar_usuario():#metodo para al apretar el boton actualizar usuario actualizar la info del usuario en la bd
        global connection,id_usuario
        try:
           cursor = connection.cursor()
           username = entry_username.get()
           permisos = box_permisos.get()
           estatus = box_estatus.get()
           email = entry_email.get()
           nombre_completo = entry_nombre.get()
           telefono = entry_telefono.get()
           
           if username == "" or email == "" or nombre_completo == "" or telefono == "":
               messagebox.showinfo("!","Debes llenar todos los campos")
           else:    
           
             sql = "UPDATE usuarios set nombre_usuario = '{}', permisos = '{}', estatus = '{}', email = '{}', nombre_completo = '{}', telefono = '{}' where ID = '{}'".format(
                 username.replace(" ",""),
                 permisos,
                 estatus,
                 email.replace(" ",""),
                 nombre_completo,
                 telefono.replace(" ",""),
                 id_usuario
             )
             cursor.execute(sql)
             connection.commit()
             messagebox.showinfo("Correcto","Usuario Actualizado correctamente")
        except:
            messagebox.showinfo("Error","Error al conectar con la BD")   
    def boton_borrar_usuario():
        global connection,id_usuario
        try:
           cursor = connection.cursor()
           sql = "DELETE from usuarios where ID = '{}'".format(id_usuario)
           respuesta = messagebox.askquestion("!","Estas seguro de eliminar el usuario??")
           if respuesta=="yes":
              cursor.execute(sql)
              connection.commit() 
              messagebox.showinfo("!","Usuario borrado correctamente")
              raiz.destroy()
           else:
               pass    
        except:
            messagebox.showinfo("Error","Error al borrar al usuario")  
            
    def boton_restaurar_pass():
        import Restaurar_Password
        restaurar = Restaurar_Password
        restaurar.main(id_usuario)              
    
    boton_actualizar_usuario = Button(frame,text="Actualizar Usuario",command=boton_actualizar_usuario)
    boton_actualizar_usuario.place(x=10,y=300)
    
    boton_restaurar_pass = Button(frame,text="Restaurar Password",command = boton_restaurar_pass)
    boton_restaurar_pass.place(x=150,y=300)
    
    boton_borrar_usuario = Button(frame,text="Borrar Usuario",command = boton_borrar_usuario)
    boton_borrar_usuario.place(x=300,y=300)
    
    raiz.mainloop()
def obtener_info_usuario(id):
        """_summary_
           obtenemos la info del usuario de la base de datos mediante el 
           id 
        Args:
            id (_type_): _description_: get from Gestionar_Usuarios.py
        """
        global connection, usuario,id_usuario
        id_usuario = id
        try:
           cursor = connection.cursor()
           sql = "SELECT * from usuarios where ID = '{}'".format(id_usuario)
           cursor.execute(sql)
           info_usuario = cursor.fetchall() 
           for usuario in info_usuario:
               pass
        except:
            messagebox.showinfo("Error","Error al conectar con la BD")
        main()  
         