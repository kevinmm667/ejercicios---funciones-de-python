def pedir_datos ():
    radio = float (input ("digite el valor del radio: "))
    
    return radio

def calcular_area (radio):
    pi= 3.14159
    area = pi * radio**2
    return area

def mostrar_resultado(area):
    print ("el area del circulo es: ", area)
    
#***********codigo principal*********

datos = pedir_datos()
calculo = calcular_area (datos)
resultado = mostrar_resultado (calculo)