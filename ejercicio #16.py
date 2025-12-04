#zona de funciones
def pedir_lado():
    lado1 = float(input("ingrese el valor del lado del cubo: "))
    return lado1

def calcular_volumen(lado1):
    volumen = lado1**3
    return volumen

def mostrar_mensaje(volumen):
    print ("el volumen del cubo es: ", volumen)
    
#**********codigo principal****************

lado = pedir_lado()
volumen = calcular_volumen(lado)
resultado = mostrar_mensaje(volumen)
