def pedir_altura():
    altura = float (input ("dgite el valor de la alura del cono: "))
    return altura

def pedir_radio():
    radio_base= float (input("digite el valor del radio de la base del cono: "))
    return radio_base

def calcular_volumen (altura, radio_base):
    pi= 3.14159
    volumen = (1/3) * pi *(radio_base**2) * altura
    return volumen

def mostrar_resultado(volumen):
    print ("el volumen del cono es: ", volumen)
    
#************codigo principal****************

altura= pedir_altura()
radio_base = pedir_radio()
calculo = calcular_volumen (altura, radio_base)
resultado = mostrar_resultado(calculo)    