def redimensionar(imagen_una_fila, num_columnas):
  '''
    Recibe como entrada la lista imagen_una_fila de una dimensión
    y retorna una lista de listas, cada una de longitud num_columnas,
    conteniendo los valores de imagen_una_fila.
    '''
  lista_vacia = []
  for i in range(0, len(imagen_una_fila), num_columnas):
    lista_vacia.append(imagen_una_fila[i:i + num_columnas])
  return lista_vacia

def reflejar_vertical(matriz):
  '''
    Retorna una copia de matriz invirtiendo el orden de sus filas.
    '''

  return matriz[::-1]

def reflejar_horizontal(matriz):
  '''
    Retorna una copia de matriz invirtiendo el orden de sus columnas.
    '''
  for i in range(len(matriz)):
    matriz[i] = matriz[i][::-1]
  return matriz


def crear_collage(matriz):
  '''
    Sean F y C la cantidad de filas y columnas de matriz, respectivamente.
    Esta función retorna una matriz collage de tamaño 2F x 2C.
    Las primeras F filas y C columnas de collage contienen una copia de matriz.
    Las filas 0 a F-1 y las columnas C a 2C-1 de collage contienen una copia
    de matriz reflejada horizontalmente. Las filas F a 2F-1 y las columnas
    0 a C-1 de collage contienen una copia de matriz reflejada verticalmente.
    Finalmente, las filas F a 2F-1 y las columnas C a 2C-1 de collage contienen
    una copia de matriz reflejada tanto horizontal como verticalmente.
    '''
  lista = []
  for i in range(len(matriz)):
    lista.append(matriz[i] + matriz[i][::-1])
  lista += lista[::-1]
  return lista