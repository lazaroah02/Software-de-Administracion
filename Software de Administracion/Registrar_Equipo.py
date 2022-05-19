from tkinter import *
from tkinter import ttk,messagebox
from mis_librerias import Centrar_Ventana,Connection_BD,RGB

def main(cliente,id,user):
    nombre_cliente = cliente
    id_cliente = id
    usuario = user
    rgb = RGB
    centrar = Centrar_Ventana
    raiz = Tk()
    raiz.geometry(centrar.centrar_ventana(500,500,raiz))
    raiz.title("Registrar nuevo equipo para " + nombre_cliente)
    
    frame = Frame(raiz)
    frame.config(bg = rgb.RGB((84,146,203)))
    frame.pack(fill = "both",expand=True)
    
    label_nombre_cliente = Label(frame,text="Cliente")
    label_nombre_cliente.config(bg=rgb.RGB((84,146,203)))
    label_nombre_cliente.grid(row = 0,column =0,padx=10,pady=10,sticky="w")
    
    entry_nombre_cliente = Entry(frame)
    entry_nombre_cliente.insert(INSERT,nombre_cliente)
    entry_nombre_cliente.config(state=DISABLED,width=25)
    entry_nombre_cliente.grid(row=0,column=1,sticky="w")
    
    label_tipo = Label(frame,text="Tipo")
    label_tipo.config(bg=rgb.RGB((84,146,203)))
    label_tipo.grid(row = 1,column =0,padx=10,pady=10,sticky="w")
    
    box_tipo = ttk.Combobox(frame,values=("Laptop","Desktop","Tablet","Smartphone"))
    box_tipo.config(state="readonly",width=22)
    box_tipo.set("Laptop")
    box_tipo.grid(row = 1,column = 1,sticky="w")
    
    label_marca = Label(frame,text="Marca")
    label_marca.config(bg=rgb.RGB((84,146,203)))
    label_marca.grid(row = 2,column =0,padx=10,pady=10,sticky="w")
    
    entry_marca = Entry(frame)
    entry_marca.config(width=25)
    entry_marca.grid(row = 2,column = 1,sticky="w")
    
    label_modelo = Label(frame,text="Modelo")
    label_modelo.config(bg=rgb.RGB((84,146,203)))
    label_modelo.grid(row = 3,column =0,padx=10,pady=10,sticky="w")
    
    entry_modelo = Entry(frame)
    entry_modelo.config(width=25)
    entry_modelo.grid(row = 3,column = 1,sticky="w")
    
    label_observaciones = Label(frame,text="Observaciones")
    label_observaciones.config(bg=rgb.RGB((84,146,203)))
    label_observaciones.grid(row = 4,column =0,padx=10,pady=10,sticky = "n")
    
    text_observaciones = Text(frame)
    text_observaciones.config(width=45,height=10)
    text_observaciones.grid(row = 4,column =1,pady=10)
    
    scroll = Scrollbar(frame,command=text_observaciones.yview)
    scroll.grid(row = 4,column =2,padx=5,pady=10,sticky="nsew")
    text_observaciones.config(yscrollcommand=scroll.set)
    
    def codigo_boton_agregar(event):
        if entry_marca.get() == "" :
            entry_marca.config(bg ="red")
            messagebox.showinfo("Error","Debes ingresar el nombre")
            entry_marca.config(bg ="white")
        elif entry_modelo.get() == "":
            entry_modelo.config(bg ="red")
            messagebox.showinfo("Error","Debes ingresar el modelo")
            entry_modelo.config(bg ="white")
        else:
            try:
               conect = Connection_BD
               connection = conect.connection()
               cursor = connection.cursor()
               sql = "INSERT into equipos values(NULL,'{}','{}','{}','{}','{}','{}')".format(
                   id_cliente,
                   entry_marca.get(),
                   box_tipo.get(),
                   entry_modelo.get(),
                   text_observaciones.get(1.0,"end"),
                   "Nuevo Ingreso"
               )    
               cursor.execute(sql)
               connection.commit()
               messagebox.showinfo("!","El equipo se agrego correctamente")
               raiz.destroy()
               import Informacion_Clientes
               info = Informacion_Clientes
               info.obtener_info_cliente(id_cliente,usuario)
               
            except:
                messagebox.showinfo("!","Error al conectar con la base de datos")   
            
    
    boton_agregar = Button(frame,text="Agregar Equipo",command=lambda:codigo_boton_agregar(""))
    boton_agregar.place(x=150,y=400)
    
    raiz.mainloop()
