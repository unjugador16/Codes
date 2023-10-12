DIAS_ENERO = 31
DIAS_FEBRERO = 28
DIAS_MARZO = 31
DIAS_ABRIL = 30
DIAS_MAYO = 31
DIAS_JUNIO = 30
DIAS_JULIO = 31
DIAS_AGOSTO = 31
DIAS_SEPTIEMBRE = 30
DIAS_OCTUBRE = 31
DIAS_NOVIEMBRE = 30
DIAS_DICIEMBRE = 31

DIAS_FEBRERO_BISIESTO = 29

DIA_ANHO_NUEVO = 1
MES_ANHO_NUEVO = 1

DIA_DIA_TRABAJO = 1
MES_DIA_TRABAJO = 5

DIA_NAVIDAD = 24
MES_NAVIDAD = 12

DIA_FIN_ANHO = 31
MES_FIN_ANHO = 12

DIAS_ANHO = [DIAS_ENERO,DIAS_FEBRERO,DIAS_MARZO,DIAS_ABRIL,DIAS_MAYO,DIAS_JUNIO,DIAS_JULIO,DIAS_AGOSTO,DIAS_SEPTIEMBRE,DIAS_OCTUBRE,DIAS_NOVIEMBRE,DIAS_DICIEMBRE]

def es_bisiesto(a):
    """Retorna True si el año ingresado es bisiesto, y False si no es bisiesto"""  
    if (a%4==0 and a%100 != 0) or (a%100 == 0 and a%400 == 0):
        return True
    else:
        return False

def dias_mes(m,a):
    """Recibe dos números, mes y año (m,a) y devuelve la cantidad de dias del mes del año ingresado"""
    if m == 2 and es_bisiesto(a) == True:
        return DIAS_FEBRERO_BISIESTO
    elif m == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        return DIAS_ENERO
    elif m == 4 or 6 or 9 or 11:
        return DIAS_ABRIL
    else:
        return DIAS_FEBRERO

def fecha_valida(d, m, a):
    """Devuelve True si la fecha(d,m,a) si existe y si no devuelve False"""
    d,m = int(d), int(m)
    if 1<=m<=12 and 1 <= d <= dias_mes(m,a):
        return True
    else:
        return False

def dias_transcurridos(d,m,a):
    """Retorna el núemro de dias entre el primero de enero del año ingresado y la fecha ingresada"""
    x = d
    if es_bisiesto(a) == True and m > 2:
        x += 1
    for i in range(m-1):
        x += DIAS_ANHO[i]
    return x

def es_igual(d1, m1, a1, d2, m2, a2):
    """Retorna True si d1/m1/a1 y d2/m2/a2 es la misma fecha, en caso contrario retorna False """
    if d1 == d2 and m1 == m2 and a1 == a2:
        return True
    else:
        return False

def es_anterior(d1, m1, a1, d2, m2, a2):
    """Retorna True si la fecha d1/m1/a1 ocurrió antes que la fecha d2/m2/a2, en caso contraio retorna False"""
    if es_igual(d1, m1, a1, d2, m2, a2) == False:
        y = 0
        x = 0
        for i in range(4,a1+1,4):
            if es_bisiesto(i) == True:
                y += 1
        for i in range(4,a2+1,4):
            if es_bisiesto(i) == True:
                x += 1
        a = ((a1*365)+(y)+(dias_transcurridos(d1,m1,a1)))
        b = ((a2*365)+(x)+(dias_transcurridos(d2,m2,a2)))
        print(a,b,b-a) #antes del año 2000 se le suma 1 al número de dias de diferencia
        #return ((a1*365)+(y)+(dias_transcurridos(d1,m1,a1)))<((a2*365)+(x)+(dias_transcurridos(d2,m2,a2)))
    else:
        return False

def es_posterior(d1, m1, a1, d2, m2, a2):
    """Retorna True si la fecha d1/m1/a1 ocurrió después de la fecha d2/m2/a2, en caso contrario retorna False"""
    return not es_anterior(d1, m1, a1, d2, m2, a2)

print(es_anterior(1, 2, 1899, 8, 9, 1998))
print(es_anterior(1, 2, 1899, 2, 2, 1899))
print(es_bisiesto(2000))