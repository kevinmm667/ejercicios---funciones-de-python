def pedir_longitud():
    long = float (input("digite la longitud del rectangulo: "))
    return long

def pedir_ancho():
    ancho = float (input("digite el ancho del rectangulo: "))
    return ancho

def procesar_datos(long, ancho):
    area = long * ancho
    return area

def imprimir_mensaje(area):
    print ("el area del rectangulo es: ", area)
    
#**************codigo principal***************

longitud = pedir_longitud()
ancho = pedir_ancho()
area = procesar_datos (longitud, ancho)
mensaje = imprimir_mensaje (area)
