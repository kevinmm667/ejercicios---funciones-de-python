def pedir_base():
    base = float (input("digite el valor de la base del rectangulo: "))
    return base

def pedir_altura():
    altura = float (input ("digite el valor de la altura del rectangulo: "))
    return altura

def calcular_area(altura, base):
    area = altura * base
    return area

def mostrar_resultado(area):
    print ("el area del rectangulo es: ", area)
    
#*************codigo principal************

base = pedir_base()
altura = pedir_altura()
calculo = calcular_area(altura, base)
mostrar_resultado(calculo)