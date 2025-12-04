def pedir_Kl():
    kilometros = float (input("digite la cantidad de kilometros para convertir a millas: "))
    return kilometros

def procesar_datos(kilometros):
    millas = 0.621
    convercion = kilometros * millas
    return convercion 

def imprimir_mensaje(convercion):
    print ("los kilometros digitados a millas son: ", convercion ) 
    
#***************codigo principal****************

KL = pedir_Kl()
calculo = procesar_datos(KL)
mensaje = imprimir_mensaje (calculo)