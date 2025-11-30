def pedir_base():
    r_base = float (input("digite el radio de la base del cilindro: "))
    return r_base

def pedir_altura():
    altura =float (input("digite la altura del cilindro: "))
    return altura

def calcular_volumen (r_base, altura):
    pi = 3.14159
    volumen = (pi * altura * (r_base**2))
    return volumen

def imprimir_resultado(volumen):
    print ("el volumen del cilindro es: ", volumen)
    
#**********codigo principal***************

r_base = pedir_base()
altura = pedir_altura()
resultado = calcular_volumen(r_base, altura)
imprimir_resultado (resultado)
    