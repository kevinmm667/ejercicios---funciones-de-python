#********zona de funciones****

def pedir_radio():
    radio = float (input("digite el valor del radio: "))
    return radio

def calcular_volumen (radio):
    pi = 3.14159
    volumen = (4/3 * pi * (radio**3))
    return volumen

def mostrar_resultado (volumen):
    print ("el volumen de la esfera es: ", volumen)
    
#*************zona de codigo principal************

radio = pedir_radio()
calculo = calcular_volumen(radio)
mostrar_resultado (calculo)
    
