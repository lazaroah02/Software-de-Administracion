
from tkinter import *
from mis_librerias import Centrar_Ventana,RGB
import os,sys
def main(a):
    centrar = Centrar_Ventana
    rgb = RGB
    usuario = a
    raiz = Tk()
    raiz.title("Administrador -- Sesion de: " + usuario)
    raiz.geometry(centrar.centrar_ventana(600, 500, raiz))#centramos la ventana utilizando un metodo de Centrar_Ventana 
    raiz.resizable(0, 0)

    frame = Frame(raiz)
    frame.config(bg = rgb.RGB((84,146,203)))
    frame.pack(fill="both", expand=True)

    label_encabezado = Label(frame, text="Bienvenido " + usuario)
    label_encabezado.config(width=40, font=18,bg= rgb.RGB((84,146,203)))
    label_encabezado.place(x=80, y=10)

    # Metodos para los evento de los botones
    def codigo_boton_calculadora():
        import Calculadora
       

    def codigo_boton_gestionar_usuario():
        import Gestionar_Usuarios
        gestionar = Gestionar_Usuarios
        gestionar.main(usuario)

    def codigo_boton_registrar_usuario():#llama la interfaz Registrar_Usuario
        import Registrar_Usuarios
        registrar = Registrar_Usuarios
        registrar.main(usuario)

    def codigo_boton_vista_capturista():#llama a la interfaz Capturista
        import Capturista
        capturista = Capturista
        capturista.main(usuario,Toplevel())

    def codigo_boton_vista_tecnico():#llama la interfaz Tecnico
        import Tecnico
        tecnico = Tecnico
        tecnico.main(usuario,Toplevel())

    def codigo_boton_info():
        import Acerca_de
        info = Acerca_de
        info.main()
    # Botones
    imagen = PhotoImage(file="Imagenes/addUser.png")
    boton_registrar_usuario = Button(frame, command=codigo_boton_registrar_usuario)
    boton_registrar_usuario.config(image=imagen,width=90, height=95)
    boton_registrar_usuario.place(x=50, y=100)

    imagen1 = PhotoImage(file="Imagenes/informationuser.png")
    boton_gestionar_usuario = Button(frame,command=codigo_boton_gestionar_usuario)
    boton_gestionar_usuario.config(image=imagen1,width=90, height=95)
    boton_gestionar_usuario.place(x=250, y=100)

    imagen2 = PhotoImage(file="Imagenes/calculadora.png")
    boton_Calculadora = Button(frame, command=codigo_boton_calculadora)
    boton_Calculadora.config(image=imagen2,width=90, height=95)
    boton_Calculadora.place(x=450, y=100)

    imagen3 = PhotoImage(file="Imagenes/capturista.png")
    boton_vista_capturista = Button(frame,command=codigo_boton_vista_capturista)
    boton_vista_capturista.config(image=imagen3,width=90, height=95)
    boton_vista_capturista.place(x=50, y=300)

    imagen4 = PhotoImage(file="Imagenes/tecnico.png")
    boton_vista_tecnico = Button(frame,command = codigo_boton_vista_tecnico)
    boton_vista_tecnico.config(image=imagen4,width=90, height=95)
    boton_vista_tecnico.place(x=250, y=300)

    imagen5 = PhotoImage(file="Imagenes/info.png")
    boton_info = Button(frame,command=codigo_boton_info)
    boton_info.config(image=imagen5,width=90, height=95)
    boton_info.place(x=450, y=300)

    label_registrar_usuario = Label(frame, text="Registrar usuario")
    label_registrar_usuario.config(bg= rgb.RGB((84,146,203)))
    label_registrar_usuario.place(x=50, y=205)

    label_gestionar_usuario = Label(frame, text="Gestionar usuario")
    label_gestionar_usuario.config(bg= rgb.RGB((84,146,203)))
    label_gestionar_usuario.place(x=250, y=205)

    label_Calculadora = Label(frame, text="Calculadora")
    label_Calculadora.config(bg= rgb.RGB((84,146,203)))
    label_Calculadora.place(x=450, y=205)

    label_vista_capturista = Label(frame, text="Vista Capturista")
    label_vista_capturista.config(bg= rgb.RGB((84,146,203)))
    label_vista_capturista.place(x=50, y=405)

    label_vista_tecnico = Label(frame, text="Vista Tecnico")
    label_vista_tecnico.config(bg= rgb.RGB((84,146,203)))
    label_vista_tecnico.place(x=250, y=405)

    label_info = Label(frame, text="Acerca de:")
    label_info.config(bg= rgb.RGB((84,146,203)))
    label_info.place(x=450, y=405)

    raiz.mainloop()


