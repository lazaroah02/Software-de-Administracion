from tkinter import *
from mis_librerias import Centrar_Ventana,Connection_BD,RGB
from tkinter import messagebox as MessageBox
id = []
nombre_usuario = ""
def main(usuario):
    global nombre_usuario
    rgb = RGB
    centrar = Centrar_Ventana
    nombre_usuario = usuario
    raiz = Tk()
    raiz.title("Clientes Registrados -- Sesion de: " + nombre_usuario)
    raiz.geometry(centrar.centrar_ventana(900,500,raiz))
    raiz.resizable(0,0)
    
    frame = Frame(raiz)
    frame.config(bg=rgb.RGB((84,146,203)))
    frame.pack(fill="both",expand=True)
    
    label_encabezado = Label(frame,text="Clientes Registrados")
    label_encabezado.config(font=18,width=25,bg=rgb.RGB((84,146,203)))
    label_encabezado.place(x=250,y=10)
    
    text = Text(frame)
    text.config(width=93,height=20,font=("Courier",11,"italic"))
    text.grid(row=2,column=2,padx=10,pady=60)
    text.insert(INSERT," ID     NOMBRE    EMAIL     TELEFONO ")
    text.insert(INSERT,"\n \n")
    
    scroll = Scrollbar(frame,command=text.yview)
    scroll.grid(row=2,column=3,padx = 10,pady=55,sticky="nsew")
    text.config(yscrollcommand=scroll.set)
    
    label_id = Label(frame,text="ID del cliente")
    label_id.config(bg=rgb.RGB((84,146,203)))
    label_id.place(x=50,y=450)
    
    entry_id = Entry(frame)
    entry_id.place(x=150,y=450)
    
    #Coneccion con bd
    def connexion():
        global id
        conect = Connection_BD
        try:
           connection = conect.connection()
           cursor = connection.cursor()
           sql = "SELECT ID_cliente, nombre_cliente, email_cliente, tel_cliente FROM clientes"
           cursor.execute(sql)
           datos_bd = cursor.fetchall()
           
           if datos_bd == None:
               MessageBox.showinfo("Error","No hay usuarios registrados en la BD")
           else:
                 for datos in datos_bd:
                     text.insert(INSERT," {}".format(datos)) 
                     text.insert(INSERT,"\n \n")
                     id.append(datos[0])
                 text.config(state="disabled")  
                      
                              
        except:
             MessageBox.showinfo("Error","Error al conectar con la base de datos")
    connexion()
    def codigo_boton(event):
        global id,nombre_usuario
        if entry_id.get() == "" :
                MessageBox.showinfo("Error","Debes ingresar un ID valido ")
        else:  
            try:      
                a = int(entry_id.get()) 
                b = a in id
            except:
                MessageBox.showinfo("Error","Debes ingresar un ID valido no puede ser una letra o simbolo")              
            if  b == False:
                    MessageBox.showinfo("Error","Debes ingresar un ID valido") 
            else:
                import Informacion_Clientes
                info = Informacion_Clientes
                raiz.destroy()
                info.obtener_info_cliente(a,nombre_usuario)                   
                       
    boton = Button(frame,text="Aceptar",command=lambda:codigo_boton(""))
    raiz.bind("<Return>",codigo_boton)
    boton.place(x=300,y=447)     
    raiz.mainloop()
   