from tkinter import *

#============================================= Menu ==============================================#

ventana = Tk()
ventana.option_add('*Font', 'Verdana 10') # cambia la letra y su tamaño
barra_menu = Menu(ventana) # crea una barra de menu en la parce superior de la ventana
ventana.config(menu= barra_menu, width= 600, height= 400) # no se le coloca el ventana.geometry porque toma automaticamente estas dimensiones 

menu_archivo = Menu(barra_menu, tearoff= 0) # tearoff es para que se quiten unas lineas en el menú
menu_archivo.add_command(label= 'Nuevo')
menu_archivo.add_command(label= 'Abrir')
menu_archivo.add_command(label= 'Guardar')
menu_archivo.add_command(label= 'Guardar Como...')
menu_archivo.add_separator() # se crea una linea separadora
menu_archivo.add_command(label= 'Cerrar')
barra_menu.add_cascade(label= 'Archivo', menu= menu_archivo)

menu_edit = Menu(barra_menu, tearoff= 0)
menu_edit.add_command(label= 'Cortar')
menu_edit.add_command(label= 'Pegar')
menu_edit.add_command(label= 'Imprimir')
barra_menu.add_cascade(label= 'Edición', menu= menu_edit)

menu_ayuda = Menu(barra_menu, tearoff= 0)
menu_ayuda.add_command(label= 'Soporte')
menu_ayuda.add_command(label= 'Actualizaciones')
menu_ayuda.add_command(label= 'Acerca de')
barra_menu.add_cascade(label= 'Ayuda', menu= menu_ayuda)

ventana.mainloop()