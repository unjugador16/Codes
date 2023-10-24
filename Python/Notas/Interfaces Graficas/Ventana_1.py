from tkinter import *

ventana = Tk() # es un objeto de la clase tk()

ventana.geometry('500x300') # tamaño en ancho x alto, pero se puede redimensionar manualmente
ventana.config(bg='lightblue')  # color de fondo
ventana.title('Ventana Principal') # el nombre de la ventana
ventana.resizable(width=False, height=False) # se bloquea la redimension manual

ventana.mainloop() # esto es un metodo de la clase que hace que la ventana esté todo el tiempo activa

#========================================= Ventana Label =========================================#

