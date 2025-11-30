def pedir_datos():
    lado1 = float (input ("digite el valor del lado 1: "))

    return lado1

def calcular_area(lado1):
    area = lado1**2
    return area

def mostrar_resultado(area):
    print ("el area del cuadrado es: ", area)

#*************codigo principal*****************

lado1 = pedir_datos ()
calculo = calcular_area(lado1)
resultado = mostrar_resultado(calculo)

