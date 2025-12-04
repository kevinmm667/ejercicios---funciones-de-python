def pedir_base ():
    base = float(input("ingrese el valor de la base del prisma: "))
    return base

def pedir_altura ():
    altura = float(input("ingrese el valor de la altura del prisma: "))
    return altura

def pedir_ancho ():
    ancho = float(input("ingrese el valor del ancho del prisma: "))
    return ancho

def calcular_area (base, altura, ancho):
    area = ((base * altura) /2)*ancho
    return area

def mostrar_resultado (area):
    print ("el volumen del prisma rectangular es: ", area)
    
#********codigo principal**************

base = pedir_base()
altura = pedir_altura()
ancho = pedir_ancho()
calculo = calcular_area(base, altura, ancho)
resultado = mostrar_resultado(calculo)