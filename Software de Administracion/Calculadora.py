import math
from tkinter import *
from mis_librerias import Centrar_Ventana
import math
      #Ventana
centrar = Centrar_Ventana
raiz = Tk()
raiz.title("Calculadora")

raiz.geometry(centrar.centrar_ventana(300,400,raiz))
raiz.resizable(0,0)
frame = Frame(raiz)
frame.pack(fill="both",)
frame.config(width="300",height="400",bg="#%02x%02x%02x" % (84,146,203))
     #variables Globales
tex_valor1 = ""
tex_valor2 = ""
operacion = ""
tex = tex_valor1 + operacion + tex_valor2
resultado =0
     #labels     
     
label= Label(frame)
label.place(x=50 ,y=30)
label.config(width=26,height=2,anchor="e")

label_result = Button(frame, text="")
label_result.config(width=11, height=2,anchor="e")
label_result.place(x=150, y=80)

 # metodos para las operaciones
def Suma(valor1, valor2):
        #obtenemos dos valores , los sumamos y mostramos el resultado en el label_resultado
        global resultado
        resultado = valor1 + valor2
        label_result.config(text=resultado)

def Resta(valor1, valor2):
        #obtenemos dos valores , los restamos y mostramos el resultado en el label_resultado
        global resultado
        resultado = valor1 - valor2
        label_result.config(text=resultado)

def Multiplicacion(valor1, valor2):
        #obtenemos dos valores , los multiplicamos y mostramos el resultado en el label_resultado
        global resultado
        resultado = valor1 * valor2
        label_result.config(text=resultado)

def Division(valor1, valor2):
        #obtenemos dos valores , los dividimos y mostramos el resultado en el label_resultado
        global resultado
        resultado = valor1 / valor2
        label_result.config(text=resultado)

def raiz_cuadrada(valor2):
        global resultado
        resultado = math.sqrt(valor2)
        label_result.config(text=resultado)

def Potencia(valor1, valor2):
        global resultado
        resultado = valor1 ** valor2
        label_result.config(text=resultado)

       #Evento de los botones
        """_summary_
        Metodos que contienen la logica que ocurre al presionar cada 
        boton(se guarda en una variable acumulativa de tipo str cada numero que se va tecleando para 
        luego mostrarlo en el label(pizarra))
        """
def Codigo_boton0(event):
        global tex_valor1,tex_valor2,tex,operacion
        if operacion == "":#si no se ha presionado el boton para realizar alguna operacion 
                tex_valor1 += "0"
                tex = tex_valor1 + operacion + tex_valor2
                label.config(text=tex)
        else:#si se ha presionado el boton para realizar alguna operacion 
                tex_valor2 += "0"
                tex = tex_valor1 + operacion + tex_valor2
                label.config(text=tex)
        Codigo_boton_igual()

#la logica de todos los demas metodos de los numeros son iguales al boton cero 
def Codigo_boton1(event):
        global tex_valor1,tex_valor2,tex,operacion
        if operacion == "":
                tex_valor1 += "1"
                tex = tex_valor1 + operacion + tex_valor2
                label.config(text=tex)
        else:
                tex_valor2 += "1"
                tex = tex_valor1 + operacion + tex_valor2
                label.config(text=tex)
        Codigo_boton_igual()


def Codigo_boton2(event):
        global tex_valor1,tex_valor2,tex,operacion
        if operacion == "":
                tex_valor1 += "2"
                tex = tex_valor1 + operacion + tex_valor2
                label.config(text=tex)
        else:
                tex_valor2 += "2"
                tex = tex_valor1 + operacion + tex_valor2
                label.config(text=tex)
        Codigo_boton_igual()

def Codigo_boton3(event):
        global tex_valor1,tex_valor2,tex,operacion
        if operacion == "":
                tex_valor1 += "3"
                tex = tex_valor1 + operacion + tex_valor2
                label.config(text=tex)
        else:
                tex_valor2 += "3"
                tex = tex_valor1 + operacion + tex_valor2
                label.config(text=tex)
        Codigo_boton_igual()

def Codigo_boton4(event):
        global tex_valor1,tex_valor2,tex,operacion
        if operacion == "":
                tex_valor1 += "4"
                tex = tex_valor1 + operacion + tex_valor2
                label.config(text=tex)
        else:
                tex_valor2 += "4"
                tex = tex_valor1 + operacion + tex_valor2
                label.config(text=tex)
        Codigo_boton_igual()

def Codigo_boton5(event):
        global tex_valor1,tex_valor2,tex,operacion
        if operacion == "":
                tex_valor1 += "5"
                tex = tex_valor1 + operacion + tex_valor2
                label.config(text=tex)
        else:
                tex_valor2 += "5"
                tex = tex_valor1 + operacion + tex_valor2
                label.config(text=tex)
        Codigo_boton_igual()

def Codigo_boton6(event):
        global tex_valor1,tex_valor2,tex,operacion
        if operacion == "":
                tex_valor1 += "6"
                tex = tex_valor1 + operacion + tex_valor2
                label.config(text=tex)
        else:
                tex_valor2 += "6"
                tex = tex_valor1 + operacion + tex_valor2
                label.config(text=tex)
        Codigo_boton_igual()

def Codigo_boton7(event):
        global tex_valor1,tex_valor2,tex,operacion
        if operacion == "":
                tex_valor1 += "7"
                tex = tex_valor1 + operacion + tex_valor2
                label.config(text=tex)
        else:
                tex_valor2 += "7"
                tex = tex_valor1 + operacion + tex_valor2
                label.config(text=tex)
        Codigo_boton_igual()

def Codigo_boton8(event):
        global tex_valor1,tex_valor2,tex,operacion
        if operacion == "":
                tex_valor1 += "8"
                tex = tex_valor1 + operacion + tex_valor2
                label.config(text=tex)
        else:
                tex_valor2 += "8"
                tex = tex_valor1 + operacion + tex_valor2
                label.config(text=tex)
        Codigo_boton_igual()

def Codigo_boton9(event):
        global tex_valor1,tex_valor2,tex,operacion
        if operacion == "":
                tex_valor1 += "9"
                tex = tex_valor1 + operacion + tex_valor2
                label.config(text=tex)
        else:
                tex_valor2 += "9"
                tex = tex_valor1 + operacion + tex_valor2
                label.config(text=tex)
        Codigo_boton_igual()
#metodos con la logica de los botones que contienen las operaciones
def Codigo_boton_suma(event):
    global operacion,tex,tex_valor1,tex_valor2
    if tex_valor1=="":
            tex_valor1 = "0"
    operacion = "+"
    tex = tex_valor1 + operacion + tex_valor2
    label.config(text=tex)


def Codigo_boton_resta(event):
        global operacion,tex,tex_valor1,tex_valor2
        if tex_valor1=="":
            tex_valor1 = "0"
        operacion = "-"
        tex = tex_valor1 + operacion + tex_valor2
        label.config(text=tex)

def Codigo_boton_multi(event):
        global operacion,tex,tex_valor1,tex_valor2
        if tex_valor1=="":
            tex_valor1 = "0"
        operacion = "x"
        tex = tex_valor1 + operacion + tex_valor2
        label.config(text=tex)

def Codigo_boton_division(event):
        global operacion,tex,tex_valor1,tex_valor2
        if tex_valor1=="":
            tex_valor1 = "0"
        operacion = "/"
        tex = tex_valor1 + operacion + tex_valor2
        label.config(text=tex)

def Codigo_boton_potencia():
        global operacion,tex,tex_valor1,tex_valor2
        if tex_valor1=="":
            tex_valor1 = "0"
        operacion = "^"
        tex = tex_valor1 + operacion + tex_valor2
        label.config(text=tex)
        
def Codigo_boton_raiz():
        global operacion,tex,tex_valor1,tex_valor2
        operacion = "√"
        tex = operacion + tex_valor2
        label.config(text=tex)        

def Codigo_boton_borrar():
        global label,tex,tex_valor1,tex_valor2,operacion
        if operacion == "":
                tex_valor1 = tex_valor1[:-1]
                tex = tex_valor1 + operacion + tex_valor2
                label.config(text=tex)
        elif tex_valor2 == "" and operacion != "":
                operacion = ""
                tex = tex_valor1 + operacion + tex_valor2
                label.config(text=tex)
        else:
                tex_valor2 = tex_valor2[:-1]
                tex = tex_valor1 + operacion + tex_valor2
                label.config(text=tex)
        Codigo_boton_igual()

def Codigo_boton_igual():
         global tex_valor1,tex_valor2,tex,operacion,resultado
         if operacion == "+":
               Suma(float(tex_valor1),float(tex_valor2))

         elif operacion == "-":
               Resta(float(tex_valor1),float(tex_valor2))

         elif operacion == "x":
               Multiplicacion(float(tex_valor1),float(tex_valor2))

         elif operacion == "/":
               Division(float(tex_valor1),float(tex_valor2))

         elif operacion == "^":
               Potencia(float(tex_valor1), float(tex_valor2))
               
         elif operacion == "√":
               raiz_cuadrada(float(tex_valor2)) 
                          
               

def Codigo_boton_pto(event):
        global tex_valor1,tex_valor2,tex,operacion
        if operacion == "":
                tex_valor1 += "."
                tex = tex_valor1 + operacion + tex_valor2
                label.config(text=tex)
        else:
                tex_valor2 += "."
                tex = tex_valor1 + operacion + tex_valor2
                label.config(text=tex)

def Codigo_boton_limpiar():#limpiamos todos los widgets y variables al presionar el boton C(reset)
        
        global tex_valor1,tex_valor2,tex,operacion
        tex_valor1 = ""
        tex_valor2 = ""
        operacion = ""
        tex = tex_valor1 + operacion + tex_valor2

        label.config(text="")
        label_result.config(text="")

        #Botones de la interfaz
boton0 = Button(frame, text = "0", command = lambda:Codigo_boton0("") )
boton0.config(width=4, height=2)
boton0.place(x=50, y=330)

boton_pto = Button(frame, text=".", command = lambda:Codigo_boton_pto(""))
boton_pto.config(width=4, height=2)
boton_pto.place(x=100, y=330)

boton_limpiar = Button(frame, text="C",command=Codigo_boton_limpiar)
boton_limpiar.config(width=4, height=2)
boton_limpiar.place(x=150, y=330)

boton_borrar = Button(frame, text="<-",command=Codigo_boton_borrar)
boton_borrar.config(width=4, height=2)
boton_borrar.place(x=150, y=130)

boton_suma = Button(frame, text="+", command =lambda: Codigo_boton_suma(""))
boton_suma.config(width=4, height=2)
boton_suma.place(x=200, y=180)

boton_resta = Button(frame, text="-", command = lambda:Codigo_boton_resta(""))
boton_resta.config(width=4, height=2)
boton_resta.place(x=200, y=230)

boton_multi = Button(frame, text="x", command = lambda:Codigo_boton_multi(""))
boton_multi.config(width=4, height=2)
boton_multi.place(x=200, y=280)

boton_div = Button(frame, text="/", command = lambda:Codigo_boton_division(""))
boton_div.config(width=4, height=2)
boton_div.place(x=200, y=330)

boton_igual = Button(frame, text="=", command = Codigo_boton_igual)
boton_igual.config(width=11, height=2)
boton_igual.place(x=50, y=130)

boton_potencia = Button(frame, text="^", command = Codigo_boton_potencia)
boton_potencia.config(width=4, height=2)
boton_potencia.place(x=200, y=130)

boton_raiz = Button(frame, text="√", command = Codigo_boton_raiz)
boton_raiz.config(width=4, height=2)
boton_raiz.place(x=250, y=130)
          #Numeros
boton1 =Button(frame,text="1",command= lambda:Codigo_boton1(""))
boton1.config(width=4,height=2)
boton1.place(x = 50,y = 280)

boton2 = Button(frame, text="2",command= lambda:Codigo_boton2(""))
boton2.config(width=4, height=2)
boton2.place(x=100, y=280)

boton3 = Button(frame, text="3",command= lambda:Codigo_boton3(""))
boton3.config(width=4, height=2)
boton3.place(x=150, y=280)

boton4 = Button(frame, text="4",command= lambda:Codigo_boton4(""))
boton4.config(width=4, height=2)
boton4.place(x=50, y=230)

boton5 = Button(frame, text="5",command= lambda:Codigo_boton5(""))
boton5.config(width=4, height=2)
boton5.place(x=100, y=230)

boton6 = Button(frame, text="6",command= lambda:Codigo_boton6(""))
boton6.config(width=4, height=2)
boton6.place(x=150, y=230)

boton7 = Button(frame, text="7",command= lambda:Codigo_boton7(""))
boton7.config(width=4, height=2)
boton7.place(x=50, y=180)

boton8 = Button(frame, text="8",command= lambda:Codigo_boton8(""))
boton8.config(width=4, height=2)
boton8.place(x=100, y=180)

boton9 = Button(frame, text="9",command= lambda:Codigo_boton9(""))
boton9.config(width=4, height=2)
boton9.place(x=150, y=180)

#mapeo de teclas para utilizar los numeros y simbolos del teclado para interactuar 
# con el programa igual que con los botones de la interfaz
raiz.bind("<Key-1>",Codigo_boton1)
raiz.bind("<Key-2>",Codigo_boton2)
raiz.bind("<Key-3>",Codigo_boton3)
raiz.bind("<Key-4>",Codigo_boton4)
raiz.bind("<Key-5>",Codigo_boton5)
raiz.bind("<Key-6>",Codigo_boton6)
raiz.bind("<Key-7>",Codigo_boton7)
raiz.bind("<Key-8>",Codigo_boton8)
raiz.bind("<Key-9>",Codigo_boton9)
raiz.bind("<Key-0>",Codigo_boton0)
raiz.bind("<Key-+>",Codigo_boton_suma)
raiz.bind("<Key-->",Codigo_boton_resta)
raiz.bind("<Key-*>",Codigo_boton_multi)
raiz.bind("<Key-/>",Codigo_boton_division)
raiz.bind("<Key-.>",Codigo_boton_pto)




raiz.mainloop()










