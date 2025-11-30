def pedir_longitud():
    long_base = float(input("digite la longitud de la base de la piramide: "))
    return long_base

def pedir_ancho():
    ancho = float(input("digite el ancho de la piramide: "))
    return ancho

def pedir_altura():
    altura = float (input("digite la altura de la piramide: "))
    return altura

def calcular_volumen(long_base, ancho, altura):
    volumen = (long_base * ancho * altura) /3
    return volumen

def mostrar_resultado (volumen):
    print ("el volumen de la piramide es: ", volumen," cm3")

#**************codigo principal**********************
longitud = pedir_longitud()
ancho = pedir_ancho()
altura = pedir_altura()
volumen = calcular_volumen(longitud, ancho, altura)
resultado = mostrar_resultado (volumen)