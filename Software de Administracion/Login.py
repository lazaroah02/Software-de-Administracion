
from tkinter import *
from tkinter import messagebox as MessageBox
from mis_librerias import RGB
from mis_librerias.Centrar_Ventana import centrar_ventana
from mis_librerias.Connection_BD import connection
def main():
    rgb = RGB
    raiz = Tk()
    raiz.title("Login")
    raiz.geometry(centrar_ventana(400,500,raiz))
    raiz.resizable(0,0)
    
    frame = Frame(raiz)
    frame.config(width=400,height=500,bg=rgb.RGB((84,146,203)))
    frame.pack(fill="both",expand=True)
    
    label_encabezado = Label(frame,text="Inicio de Sesion")
    label_encabezado.config(font=("Courtier",18,"italic"),width=25,bg=rgb.RGB((84,146,203)))
    label_encabezado.place(x=17,y=30)
    
    imag = PhotoImage(file="Imagenes/opciones.png")
    label_imagen = Label(frame,image=imag)
    label_imagen.config(width=100,height=100)
    label_imagen.place(x=150,y=80)
    
    label_usuario = Label(frame,text="Usuario")
    label_usuario.config(bg=rgb.RGB((84,146,203)))
    label_usuario.place(x=50,y=250)
    
    entry_usuario = Entry(frame)
    entry_usuario.config(width=25)
    entry_usuario.place(x=150,y=250)
    
    label_pass = Label(frame,text="Password")
    label_pass.config(bg=rgb.RGB((84,146,203)))
    label_pass.place(x=50,y=300)
    
    entry_pass = Entry(frame)
    entry_pass.config(show="*",width=25)
    entry_pass.place(x=150,y=300)
    
    def Codigo_Boton(event):
        """
        *al presionar enter o el boton conectamos con la base de datos y comprobamos el usuario y la contrasena y si es correcta
        entramos en una interfaz diferente dependiendo del nivel de permisos que tenga el usuario (Administrador, Capturista,Tecnico)
         
        """
        
        if  entry_usuario.get() == "": 
            entry_usuario.config(bg="red")
            MessageBox.showinfo("Error","Debes llenar todos los campos")
            entry_usuario.config(bg="white") 
        elif entry_pass.get() == "" : 
            entry_pass.config(bg="red")
            MessageBox.showinfo("Error","Debes llenar todos los campos")
            entry_pass.config(bg="white")     
        else:
            #instancio la clase conect
            try:
                coneccion = connection() #establezco coneccion con la bd mediante el metodo connection
                cursor = coneccion.cursor()
                sql = "SELECT nombre_usuario, pass, permisos, estatus, nombre_completo FROM usuarios where nombre_usuario = '{}' ".format(entry_usuario.get())
                cursor.execute(sql)
                user = cursor.fetchone()
                if user == None:
                    entry_usuario.config(bg="red")
                    MessageBox.showinfo("Error","User incorrect")
                    entry_usuario.config(bg="white")
                elif user[3] == "Inactivo":
                    MessageBox.showinfo("Error","El usuario ha sido deshabilitado")    
                elif user[1] != entry_pass.get():
                        entry_pass.config(bg="red")
                        MessageBox.showinfo("Error","Wrong Password")
                        entry_pass.config(bg="white")
                else:
                    if user[2] == "Administrador":
                            import Administrador
                            admin = Administrador
                            raiz.destroy()
                            admin.main(user[4])
                    elif user[2] == "Capturista":
                        import Capturista
                        capturista = Capturista
                        raiz.destroy()
                        capturista.main(user[4],Tk()) 
                    elif user[2] == "Tecnico":
                        import Tecnico
                        tec = Tecnico
                        raiz.destroy()
                        tec.main(user[4],Tk())           
                            
                
            except:
                MessageBox.showinfo("Error","Error al conectar con la base de datos")      
    
    boton = Button(frame,text="Aceptar",command=lambda:Codigo_Boton("Hola"))
    boton.place(x=200,y=350)
    
    raiz.bind("<Return>",Codigo_Boton)
    
    raiz.mainloop()
main()  