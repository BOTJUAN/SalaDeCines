import customtkinter as ctk
from PIL import ImageTk, Image
from Peliculas import mostrar_info_pelicula, cargar_posters
from F_Administrador import listado_peliculas, agregar_pelicula, gestion_salas
from tkinter import messagebox
import json

ventana = ctk.CTk()

with open("usuarios", "r") as f:
    usuarios = json.load(f)

def limpiar_ventana(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()

def registro(frame):
    limpiar_ventana(frame)
    l = ctk.CTkLabel(master=frame, text="Registrarse", font=("Arial", 20))
    l.place(x=110, y=45)

    nombre = ctk.CTkEntry(master=frame, width=220, placeholder_text="Nombre de usuario")
    nombre.place(x=50, y=110)

    nueva_contraseña = ctk.CTkEntry(master=frame, width=220, placeholder_text="Nueva Contraseña", show="*")
    nueva_contraseña.place(x=50, y=165)

    confirmar_contraseña = ctk.CTkEntry(master=frame, width=220, placeholder_text="Confirmar Contraseña", show="*")
    confirmar_contraseña.place(x=50, y=220)

    crear = ctk.CTkButton(master=frame, width=180, text="Crear cuenta", corner_radius=6, fg_color="#50BC30", hover_color="#a4a4a4", command= lambda nombre_usuario=nombre, contraseña=nueva_contraseña: registrar_usuario(nombre_usuario, contraseña))
    crear.place(x=70, y=275)

def registrar_usuario(nombre_usuario, contraseña):
    nuevo_usuario = {
        "usuario": nombre_usuario.get(),
        "contraseña": contraseña.get()
    }
    usuarios.append(nuevo_usuario)
    with open("usuarios", "w") as f:
        json.dump(usuarios, f, indent=4)
    ventana_login()

def ventana_principal():   
    limpiar_ventana(ventana)
    ventana.config(background="black")
    logo = ctk.CTkLabel(ventana, text="CINEMA", bg_color="black", font=("Arial", 25, "bold"), text_color="gold")
    logo.grid(row=0, column=0, columnspan=3, pady=10)

    frame_carteleras = ctk.CTkScrollableFrame(ventana, fg_color="black")
    frame_carteleras.grid(row=1, column=0, sticky="nsew", padx=30)
    ventana.grid_rowconfigure(1, weight=1)
    ventana.grid_columnconfigure(0, weight=1)

    cargar_posters(frame_carteleras)

def menu_administrador(fondo):
    limpiar_ventana(ventana)
    fondo = ImageTk.PhotoImage(Image.open("Imagenes\\fondo.png"))
    fondo_ventana = ctk.CTkLabel(master=ventana, image=fondo)
    frame = ctk.CTkScrollableFrame(master=fondo_ventana, width=420, height=480,fg_color="transparent", corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
    fondo_ventana.pack()

    l = ctk.CTkLabel(frame, text="Funcionalidades de Administrador", font=("Arial", 25, "bold"))
    l.pack(pady=30)

    imagen = ctk.CTkImage(Image.open("Imagenes\editar.png"), size=(80,100))
    editar = ctk.CTkButton(frame, text="Editar pelicula", image=imagen, fg_color="transparent", compound="top", text_color="white", command = lambda frame=frame, menu_administrador=menu_administrador, fondo=fondo: listado_peliculas(frame, menu_administrador, fondo))
    editar.pack(side=ctk.RIGHT, pady=130)

    imagen = ctk.CTkImage(Image.open("Imagenes\camara-de-pelicula.png"), size=(80, 100))
    agregar = ctk.CTkButton(frame, text="Agregar pelicula", image=imagen, fg_color="transparent", compound="top", text_color="white", command= lambda frame=frame, menu_administrador=menu_administrador, fondo=fondo: agregar_pelicula(frame, menu_administrador, fondo))
    agregar.pack(side=ctk.LEFT, pady=130)
    
    imagen = ctk.CTkImage(Image.open("Imagenes\silla.png"), size=(80,100))
    boton = ctk.CTkButton(frame, text="Gestion de Salas", image=imagen, fg_color="transparent", compound="top", text_color="white", command= lambda frame=frame, menu_administrador=menu_administrador, fondo=fondo: gestion_salas(frame, menu_administrador, fondo))
    boton.pack()

def verificar_usuario(nombre_usuario, contraseña, fondo):
    for usuario in usuarios:
        if usuario["usuario"] == nombre_usuario.get() and usuario["contraseña"] == contraseña.get():
            messagebox.showinfo("Atencion", f"Bienvenido {usuario['usuario']}")
            ventana_principal()
    if nombre_usuario.get() == "admin" and contraseña.get() == "admin123":
        messagebox.showinfo("Atencion", "Ha ingresado como administrador")
        menu_administrador(fondo)
    else:
        messagebox.showerror("Atencion", "Credenciales incorrectas o no existentes.")
        return

def ventana_login():
    limpiar_ventana(ventana)
    ventana.geometry("920x650")
    ventana.title("CineMax")

    fondo = ImageTk.PhotoImage(Image.open("Imagenes\\fondo.png"))
    l1 = ctk.CTkLabel(master=ventana, image=fondo)
    l1.pack()

    frame = ctk.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

    l2 = ctk.CTkLabel(master=frame, text="Iniciar sesion", font=("Arial", 20))
    l2.place(x=100, y=45)

    usuario = ctk.CTkEntry(master=frame, width=220, placeholder_text="Nombre de usuario")
    usuario.place(x=50, y=110)

    contraseña = ctk.CTkEntry(master=frame, width=220, placeholder_text="Contraseña", show="*")
    contraseña.place(x=50, y=165)

    boton = ctk.CTkButton(master=frame, width=220, text="Iniciar Sesion", corner_radius=6, fg_color="#50BC30", hover_color="#a4a4a4", command= lambda nombre_usuario=usuario, contraseña=contraseña, fondo=fondo: verificar_usuario(nombre_usuario, contraseña, fondo))
    boton.place(x=50, y=240)

    registrar = ctk.CTkButton(master=frame, width=220, text="¿No tienes cuenta? Registrate", corner_radius=6, fg_color="transparent", hover_color="#a4a4a4", command= lambda frame=frame: registro(frame))
    registrar.place(x=50, y=295)
    ventana.mainloop()

ventana_login()