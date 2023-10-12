#para que funcione deben estar en la misma carpeta
#===================================== modulos de python =========================================#
import datetime #ejemplo

print(datetime.date.today())
print(datetime.timedelta(minutes=100))

from datetime import timedelta #mas especifico

print(timedelta(minutes=100))

#====================================== modulos propios ==========================================#

import myMath
 
myMath.add(7,4)
myMath.sub(7,4)
 
from myMath import add, sub #mas especifico

add(8,4)
sub(8,4)

#================================== modulos de otras personas ====================================#
#estos se descargan directamente en el interprete de python

from colorama import Fore, Style, init
init(convert=True)# init es para que en el cmd de windows de vean los colores

print(Fore.RED + 'hello world')