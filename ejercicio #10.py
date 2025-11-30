def pedir_longitud():
    longitud = float (input("digite el valor de la longitud: "))
    return longitud

def pedir_ancho():
    ancho = float (input("digite el valor del ancho: "))
    return ancho
    
def pedir_altura():
    altura = float (input("digite el valor de la altura: "))
    return altura

def calcular_area (longitud, ancho, altura):
    area = longitud * ancho * altura
    return area

def mostrar_resultado(area):
    print ("el area del prisma rectangular es: ", area)

#****************codigo principal******************

longitud = pedir_longitud()
ancho = pedir_ancho()
altura = pedir_altura()
calculo = calcular_area(longitud, ancho, altura)
area = mostrar_resultado(calculo)