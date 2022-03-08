from cProfile import label
from cgitb import text
from operator import index
from tkinter import *
from tkinter.ttk import *
from unicodedata import name
from signaturelib import services

user = None


def login():
    index = Tk()
    index.title("LOGIN")
    index.geometry("500x200")
    index.resizable(width=False, height=False)

    luser = Label(index, text="Ingrese nombre de usuario:")
    luser.pack()

    user = StringVar()
    euser = Entry(index, width=30, textvariable=user)
    euser.pack()

    lpas = Label(index, text="Password:")
    lpas.pack()

    pas = StringVar()
    epas = Entry(index, width=30, textvariable=pas, show="*")
    epas.pack()

    def iniciar_sesion():
        global user
        usuario = user.get()
        password = pas.get()
      #  user = services.get_user_login(usuario, password)
    btn1 = Button(index, text="Entrar", command=iniciar_sesion)
    btn1.pack(side=BOTTOM)

    btn2 = Button(index, text="Registrar", command=registrar)
    btn2.pack(side=BOTTOM)

    index.mainloop()


def registrar():
    index.destroy()
    Registro = Tk()
    Registro.title("Registrar")
    Registro.geometry("500x200")
    Registro.resizable(width=False, height=False)

    nombre = Label(Registro, text="Ingrese su nombre")
    nombre.pack()

    name = StringVar()
    ename = Entry(Registro, width=30, textvariable=name)
    ename.pack()

    usuario = Label(Registro, text="Ingrese un usuario")
    usuario.pack()

    user = StringVar()
    euser = Entry(Registro, width=30, textvariable=user)
    euser.pack()

    password = Label(Registro, text="Ingrese Password")
    password.pack()

    pas = StringVar()
    epas = Entry(Registro, width=30, textvariable=pas, show="*")
    epas.pack()

    def iniciar_sesion():
        global user
        usuario = user.get()
        password = pas.get()
      #  user = services.get_user_login(usuario, password)
    btnRegistro = Button(Registro, text="Registrar", command=iniciar_sesion)
    btnRegistro.pack(side=BOTTOM)

    btnInicio = Button(Registro, text="Inicio", command=login)
    btnInicio.pack(side=BOTTOM)

    Registro.mainloop()


login()
