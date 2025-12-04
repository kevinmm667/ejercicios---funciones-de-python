def pedir_lado():
    lado = float (input("ingrese el valor del lado del hezagono: "))
    return lado

def calcular_area (lado):
    area = (3*(3**0.5)/2)*(lado**2)
    return area

def mostrar_resultado(area):
    print ("el area del hexagono es: ", area)
    
#codigo principal

lado = pedir_lado()
area = calcular_area(lado)
resultado = mostrar_resultado(area)