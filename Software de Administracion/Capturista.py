from tkinter import *
from mis_librerias import Centrar_Ventana,RGB
nombre_usuario = ""
def main(usuario,tipo):
    global nombre_usuario
    tipo_raiz = tipo #recibimos el tipo de raiz segun de q ventana llamemos esta, desde administrador con toplevel para q no den conflictos las imagenes y desde login Tk
    rgb = RGB
    centrar = Centrar_Ventana
    nombre_usuario = usuario
          
    raiz = tipo_raiz
    raiz.title("Capturista -- Sesion de: " + nombre_usuario)
    raiz.geometry(centrar.centrar_ventana(500,300,raiz))
    raiz.resizable()
    
    frame = Frame(raiz)
    frame.config(bg=rgb.RGB((84,146,203)))
    frame.pack(fill="both",expand=True)
    
    label_encabezado = Label(frame,text="Bienvenido " + nombre_usuario)
    label_encabezado.config(font=("Courier",16,"italic"),width=40,bg=rgb.RGB((84,146,203)))
    label_encabezado.place(x=0,y=10)
    
    def codigo_boton_add_clientes():
        import Registrar_Clientes
        registar = Registrar_Clientes
        registar.main(nombre_usuario)
       
    def codigo_boton_ver_clientes():
        import Clientes_Registrados
        clientes = Clientes_Registrados
        clientes.main(nombre_usuario)    
    
    imag1 = PhotoImage(file="Imagenes/add.png")
    boton_add_cliente = Button(frame,image=imag1,command = codigo_boton_add_clientes)
    boton_add_cliente.config(width=100, height=100)
    boton_add_cliente.place(x=50,y=100)
    
    label_add_cliente = Label(frame,text="Add new Cliente")
    label_add_cliente.config(bg=rgb.RGB((84,146,203)))
    label_add_cliente.place(x=55,y=205)
    
    imag2 = PhotoImage(file="Imagenes/informationuser.png")
    boton_ver_clientes = Button(frame,image=imag2,command=codigo_boton_ver_clientes)
    boton_ver_clientes.config(width=100, height=100)
    boton_ver_clientes.place(x=200,y=100)
    
    label_ver_clientes = Label(frame,text="Clientes Registrados")
    label_ver_clientes.config(bg=rgb.RGB((84,146,203)))
    label_ver_clientes.place(x=197,y=205)
    
    imag3 = PhotoImage(file="Imagenes/impresora.png")
    boton_imprimir_clientes = Button(frame,image=imag3)
    boton_imprimir_clientes.config(width=100, height=100)
    boton_imprimir_clientes.place(x=350,y=100)
    
    label_imprimir_clientes = Label(frame,text="Imprimir Clientes")
    label_imprimir_clientes.config(bg=rgb.RGB((84,146,203)))
    label_imprimir_clientes.place(x=350,y=205)
    
    raiz.mainloop()
