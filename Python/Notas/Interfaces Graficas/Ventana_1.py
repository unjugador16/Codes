from tkinter import *

ventana = Tk() # es un objeto de la clase tk()

ventana.geometry('500x300') # tamaño en ancho x alto, pero se puede redimensionar manualmente
ventana.config(bg='lightblue')  # color de fondo
ventana.title('Ventana Principal') # el nombre de la ventana
ventana.resizable(width=False, height=False) # se bloquea la redimension manual
ventana.iconbitmap('Python\\Notas\\Interfaces Graficas\\python.ico') # se le pasa la ruta del icono de la ventana
 
ventana.mainloop() # esto es un metodo de la clase que hace que la ventana esté todo el tiempo activa

#============================================ Labels =============================================#

ventana = Tk()
ventana.geometry('512x712')

etiqueta = Label(ventana, text ='Hola Mundo', fg ='blue', font =('Cascadia code',18)) # texto que aparece en la ventana y se colora de azul, la fuente es Cascadia code y el tamaño es 18
etiqueta.place(x =200, y =100) # posicion del texto en la ventana, se separa de izquiera a derecha y de arriba a abajo
image = PhotoImage(file='Python\\Notas\\Interfaces Graficas\\holamundo.png') # se crea un objeto de la clase PhotoImage y se le pasa la ruta de la imagen
etiqueta2 = Label(ventana, image = image).place(y =200) # se crea una etiqueta para mostrar la imgaen y se le pasa la imagen

ventana.mainloop()

#============================================= Entry =============================================#

ventana = Tk()
ventana.geometry('300x500')
nombre_label = Label(ventana, text ='Ingrese Nombre', font =('Cascadia code',16)).place(x =10, y =50)
campo_nombre = Entry(ventana ,bg ='lightblue', bd =4) # se crea un campo de texto y se le asigna un color de fondo y un tamaño de borde
campo_nombre.place(x =10, y =90, width =100, height =30) # lugar y tamaño del campo de texto

clave_label = Label(ventana, text ='Ingrese Clave', font =('Cascadia code',16)).place(x =10, y =130)
campo_clave = Entry(ventana, show ='*', bg ='lightblue', bd =4) # show es para que no se vea lo que se escribe en el campo de texto
campo_clave.place(x =10, y =170, width =100, height =30) # 

ventana.mainloop()

#============================================ Botones ============================================#

