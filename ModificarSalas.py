import customtkinter as ctk
from tkinter import messagebox
import json

with open("info_peliculas", "r") as f:
    peliculas = json.load(f)

def seleccionar_asiento(boton_fila, boton_columna, aux_botones, sala):
	try:
		fila = int(boton_fila.get())
		columna = int(boton_columna.get())
		if 0 <= fila < 9 and 0 <= columna < 9:
			if sala[fila][columna]["text"] != "O":
				aux_botones[fila][columna].configure(text="S", fg_color="yellow", text_color="black")
			else:
				asiento_ocupado = ctk.CTkLabel(frame, text="El asiento")
		else:
			messagebox.showerror("Atencion", "Coordenadas fuera de rango")
	except ValueError:
		messagebox.showerror("Atencion", "Datos ingresados no validos")

# Boton de asiento recomendado
def asiento_recomendado(asientos, aux_botones):
	for a in range(6,-1,-1):
		centro = 7 // 2   
		if aux_botones[a][centro].cget("text") == "L":
			aux_botones[a][centro].configure(text="S", fg_color="yellow", text_color="black")
			return
		for c in range(1, 7):
			derecha = centro + c
			izquierda = centro - c
			if derecha < 7 and aux_botones[a][derecha].cget("text") == "L":
				aux_botones[a][derecha].configure(text="S", fg_color="yellow", text_color="black")
				return
			if izquierda >= 0 and aux_botones[a][izquierda].cget("text") == "L":
				aux_botones[a][izquierda].configure(text="S", fg_color="yellow", text_color="black")
				return

def reservar_asientos(sala, indice_pelicula, indice_sala, aux_botones):
	for fila in range(len(sala)):
		for columna in range(len(sala[fila])):
			if aux_botones[fila][columna].cget("text") == "S":
				sala[fila][columna]["text"] = "O"
				sala[fila][columna]["fg_color"] = "red"
				aux_botones[fila][columna].configure(text="O", fg_color="red")
	peliculas[indice_pelicula]["asientos"][indice_sala] = sala
	with open("info_peliculas", "w") as f:
		json.dump(peliculas, f, indent=4)
	
