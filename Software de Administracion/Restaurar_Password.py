from tkinter import *
from mis_librerias import Centrar_Ventana,Connection_BD,RGB
from tkinter import messagebox
id_usuario = 0
def main(id):
    rgb = RGB
    global id_usuario
    id_usuario = id
    centrar = Centrar_Ventana
    raiz = Toplevel()
    raiz.title("Restaurar Password")
    raiz.geometry(centrar.centrar_ventana(300,200,raiz))
    raiz.resizable(0,0)
    
    frame = Frame(raiz)
    frame.config(bg=rgb.RGB((84,146,203)))
    frame.pack(fill="both",expand=True)
    
    label_newpass = Label(frame,text="New Password")
    label_newpass.config(bg=rgb.RGB((84,146,203)))
    label_newpass.place(x=10,y=30)
    
    entry_newpass = Entry(frame)
    entry_newpass.place(x=130, y=30)
    
    label_confirm = Label(frame,text="Confirm Password")
    label_confirm.config(bg=rgb.RGB((84,146,203)))
    label_confirm.place(x=10,y=100)
    
    entry_confirm = Entry(frame)
    entry_confirm.place(x=130,y=100)
    
    def codigo_boton():
        global id_usuario
        conect = Connection_BD
        if entry_confirm.get() == "" :
            entry_confirm.config(bg="red")
            messagebox.showinfo("!","Debes llenar todos los campos")
            entry_confirm.config(bg="white")
        elif entry_newpass.get() == "":
            entry_confirm.config(bg="red")
            messagebox.showinfo("!","Debes llenar todos los campos")
            entry_confirm.config(bg="white")
        elif entry_newpass.get() != entry_confirm.get():
            messagebox.showinfo("!","Las contraseñas no coinciden ")
        else:        
            try:
               connection = conect.connection()
               cursor = connection.cursor()
               confirm = entry_confirm.get()
               sql = "UPDATE usuarios SET pass = '{}'  where ID = '{}'".format(confirm.replace(" ",""),id_usuario)
               cursor.execute(sql)
               connection.commit()
               messagebox.showinfo("!","Contraseña cambiada correctamente")
               raiz.destroy()
            except:
                messagebox.showinfo("!","Error")  
    
    boton = Button(frame,text="Aceptar",command=codigo_boton)
    boton.place(x=100,y=150)
    
    
    raiz.mainloop()
  