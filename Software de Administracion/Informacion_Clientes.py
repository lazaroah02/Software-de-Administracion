from tkinter import *
from pymysql import NULL
from mis_librerias import Centrar_Ventana,Connection_BD,RGB
from tkinter import ttk,messagebox
conect = Connection_BD
connection = conect.connection()
cliente =[]
equipo =[]
id_cliente = 0
usuario = ""
def main():
    global id_cliente,usuario,connection
    rgb = RGB
    centrar = Centrar_Ventana
    raiz = Tk()
    
    raiz.title("Informacion del cliente: " + cliente[1])
    raiz.geometry(centrar.centrar_ventana(700,500,raiz))
    raiz.resizable(0,0)
    
    frame = Frame(raiz)
    frame.config(bg=rgb.RGB((84,146,203)))
    frame.pack(fill="both",expand = True)
    
    label_nombre = Label(frame,text="Nombre")
    label_nombre.config(bg=rgb.RGB((84,146,203)))
    label_nombre.grid(row=0,column=0,padx=0,pady=10,sticky="w")
    
    entry_nombre = Entry(frame)
    entry_nombre.config(width=30)
    entry_nombre.insert(INSERT,cliente[1])
    entry_nombre.grid(row=0,column=1,padx=10,pady=10,sticky="w")
    
    label_email = Label(frame,text="Email")
    label_email.config(bg=rgb.RGB((84,146,203)))
    label_email.grid(row=1,column=0,padx=0,pady=0,sticky="w")
    
    entry_email = Entry(frame)
    entry_email.config(width=30)
    entry_email.insert(INSERT,cliente[2])
    entry_email.grid(row=1,column=1,padx=10,pady=10,sticky="w")
    
    label_telefono = Label(frame,text="Telefono")
    label_telefono.config(bg=rgb.RGB((84,146,203)))
    label_telefono.grid(row=2,column=0,padx=0,pady=10,sticky="w")
    
    entry_telefono = Entry(frame)
    entry_telefono.config(width=30)
    entry_telefono.insert(INSERT,cliente[3])
    entry_telefono.grid(row=2,column=1,padx=10,pady=10,sticky="w")
    
    label_ultima_modificacion = Label(frame,text='Ultima Modificacion')
    label_ultima_modificacion.config(bg=rgb.RGB((84,146,203)))
    label_ultima_modificacion.grid(row=3,column=0,padx=0,pady=10,sticky="w")
    
    entry_ultima_modificacion = Entry(frame)
    entry_ultima_modificacion.config(width=30)
    entry_ultima_modificacion.grid(row=3,column=1,padx=10,pady=10,sticky="w")
    entry_ultima_modificacion.insert(INSERT,cliente[4])
    entry_ultima_modificacion.config(state=DISABLED)
    
    label_info_equipo = Label(frame,text="Equipos Registrados")
    label_info_equipo.config(bg=rgb.RGB((84,146,203)))
    label_info_equipo.grid(row=4,column=0,padx=0,pady=10,sticky="n")
    
    text_info_equipo = Text(frame)
    text_info_equipo.config(width=70,height=14)
    text_info_equipo.grid(row=4,column=1,pady=10,padx=0)
    text_info_equipo.insert(INSERT,"ID_equipo     Marca     Tipo    Modelo   Observaciones     estatus")
    
    scroll = Scrollbar(frame,command=text_info_equipo.yview)
    scroll.grid(row=4,column=2,sticky="nsew")
    text_info_equipo.config(yscrollcommand=scroll.set)
    
    def codigo_boton_actualizar_cliente():
        global connection,id_cliente,cliente,usuario
        if entry_email.get() == "" or entry_nombre.get() == "" or entry_telefono.get() == "":
           entry_email.config(bg="red")
           entry_nombre.config(bg="red") 
           entry_telefono.config(bg="red")
           messagebox.showinfo("!","Debes llenar todos los campos")
           entry_email.config(bg="white")
           entry_nombre.config(bg="white")
           entry_telefono.config(bg="white")
        else:   
            try:
               cursor = connection.cursor()
               email = entry_email.get()
               nombre = entry_nombre.get()
               telefono = entry_telefono.get()
               usuario,
               sql = "UPDATE clientes set nombre_cliente = '{}', email_cliente = '{}', tel_cliente = '{}', ultima_modificacion = '{}' where ID_cliente = '{}'".format(
                nombre,
                email.replace(" ",""),
                telefono.replace(" ",""),
                usuario,
                id_cliente
               )
               cursor.execute(sql)
               connection.commit()
               messagebox.showinfo("Correcto","Cliente Actualizado correctamente")
               raiz.destroy()
               import Informacion_Clientes
               info = Informacion_Clientes
               info.obtener_info_cliente(id_cliente,usuario)
            except:
                messagebox.showinfo("Error","Error al conectar con la BD")   
            
    def boton_borrar_cliente():
        """_summary_
        borramos el cliente en cuestion mediante este metodo al presionar el boton , tambien realizamos un messagebox.asquestion
        para asegurarnos de que el usuario este seguro de realizar la operacion
        """
        global connection,id_cliente
        try:
           cursor = connection.cursor()
           sql1 = "DELETE from clientes where ID_cliente = '{}'".format(id_cliente)
           sql2 = "DELETE from equipos where ID_cliente = '{}'".format(id_cliente)
           respuesta = messagebox.askquestion("!","Estas seguro de eliminar el cliente??")
           if respuesta=="yes":
              cursor.execute(sql1)
              cursor.execute(sql2)
              connection.commit() 
              messagebox.showinfo("!","Cliente borrado correctamente")
              raiz.destroy()
           else:
               pass    
        except:
            messagebox.showinfo("Error","Error al borrar al cliente")  
    def boton_registrar_nuevo_equipo():
        import Registrar_Equipo
        registrar = Registrar_Equipo
        raiz.destroy()
        registrar.main(cliente[1],id_cliente,usuario)    
    
    boton_actualizar_cliente = Button(frame,text="Actualizar Cliente",command=codigo_boton_actualizar_cliente)
    boton_actualizar_cliente.place(x=50,y=450)
    
    boton_borrar_cliente = Button(frame,text="Borrar Cliente",command = boton_borrar_cliente)
    boton_borrar_cliente.place(x=340,y=450)
    
    boton_registrar_equipo = Button(frame,text="Registrar Equipo",command = boton_registrar_nuevo_equipo)
    boton_registrar_equipo.place(x=190,y=450)

    
    """
    obtenemos la informacion del equipo que corresponde al usuario en cuestion apollandonos de la variable global id que 
    corresponde al id del cliente  
    """
    cursor2 = connection.cursor()
    sql = "SELECT ID_equipo, marca, tipo, modelo, observaciones_capturista, estatus from equipos where ID_cliente = '{}'".format(id_cliente)
    cursor2.execute(sql)
    info_equipo = cursor2.fetchall()
    for equipo in info_equipo:
       text_info_equipo.insert(INSERT,"\n")
       text_info_equipo.insert(INSERT,equipo)  
       text_info_equipo.insert(INSERT,"\n")  
    text_info_equipo.config(state=DISABLED)
    raiz.mainloop()       
def obtener_info_cliente(id,nombre_usuario):
        """_summary_
        con este metodo connectamos con la bd para solicitar la informacion del cliente que queremos visualizar 
        Args:
        id (_type_): obtenemos el id del clietne que queremos visualizar de Clientes_Registrados 
        nombre_usuario (_type_): obtenemos el nombre del usuario para mostrarlo en pantalla
        """
        global connection, cliente,id_cliente,usuario
        usuario = nombre_usuario
        id_cliente = id
        try:
           cursor = connection.cursor()
           sql = "SELECT * from clientes where ID_cliente = '{}'".format(id_cliente)
           cursor.execute(sql)
           info_cliente = cursor.fetchall() 
           for cliente in info_cliente:
               pass
        except:
            messagebox.showinfo("Error","Error al conectar con la BD")
        main()  
          
        
                  
        
