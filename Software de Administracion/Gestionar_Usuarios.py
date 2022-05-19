from tkinter import *
from mis_librerias import Centrar_Ventana,Connection_BD,RGB
from tkinter import messagebox as MessageBox
id = []
def main(usuario):
    rgb = RGB
    centrar = Centrar_Ventana
    nombre_usuario = usuario
    raiz = Tk()
    raiz.title("Gestion de usuarios -- Sesion de: " + nombre_usuario)
    raiz.geometry(centrar.centrar_ventana(900,500,raiz))
    raiz.resizable(0,0)
    
    frame = Frame(raiz)
    frame.config(bg=rgb.RGB((84,146,203)))
    frame.pack(fill="both",expand=True)
    
    label_encabezado = Label(frame,text="Usuarios Registrados")
    label_encabezado.config(font=18,width=25,bg=rgb.RGB((84,146,203)))
    label_encabezado.place(x=250,y=10)
    
    text = Text(frame)
    text.config(width=93,height=20,font=("Courier",11,"italic"))
    text.grid(row=2,column=2,padx=10,pady=60)
    text.insert(INSERT," ID     USERNAME    PERMISOS      NOMBRE       ESTATUS")
    text.insert(INSERT,"\n \n")
    
    scroll = Scrollbar(frame,command=text.yview)
    scroll.grid(row=2,column=3,padx = 10,pady=55,sticky="nsew")
    text.config(yscrollcommand=scroll.set)
    
    label_user = Label(frame,text="ID del usuario")
    label_user.config(bg=rgb.RGB((84,146,203)))
    label_user.place(x=50,y=450)
    
    entry_user = Entry(frame)
    entry_user.place(x=150,y=450)
    
    
    #Coneccion con bd
    def connexion():
        """_summary_
        Conectamos con la bd y mostramos mediante un textbox todos
        los cliente sque han sido registrados para que el usuario seleccione
        el que quiere visualizar con mas detalles o hacerle alguna modificacion
        """
        global id
        conect = Connection_BD
        try:
           connection = conect.connection()
           cursor = connection.cursor()
           sql = "SELECT ID, nombre_usuario, permisos, nombre_completo, estatus FROM usuarios"
           cursor.execute(sql)
           datos_bd = cursor.fetchall()
           
           if datos_bd == None:
               MessageBox.showinfo("Error","No hay usuarios registrados en la BD")
           else:
                 c = 1
                 for datos in datos_bd:
                     text.insert(INSERT," {}".format(datos)) 
                     text.insert(INSERT,"\n \n")
                     id.append(datos[0])
                     c+=1
                 text.config(state="disabled")        
                              
        except:
             MessageBox.showinfo("Error","Error al conectar con la base de datos")
    connexion()
    def codigo_boton(event):
        """_summary_

        Args:
            event (_type_): obtenemos el id que ingreso el usuario con el entry_user y si esta en la bd le 
            mostramos en la interfaz Informacion_Usuarios la info correspondiente con ese usuario
        """
        global id
        if entry_user.get() == "" :
                MessageBox.showinfo("Error","Debes ingresar un username ")
        else:  
            try:      
                a = int(entry_user.get()) 
                b = a in id
            except:
                MessageBox.showinfo("Error","Debes ingresar un ID valido no puede ser una letra o simbolo")              
            if  b == False:
                    MessageBox.showinfo("Error","Debes ingresar un ID valido") 
            else:
                import Informacion_Usuario
                info = Informacion_Usuario
                raiz.destroy()
                info.obtener_info_usuario(a)
                 
                                  
                       
    boton = Button(frame,text="Aceptar",command=lambda:codigo_boton(""))
    raiz.bind("<Return>",codigo_boton)
    boton.place(x=300,y=447) 
      
    raiz.mainloop()
