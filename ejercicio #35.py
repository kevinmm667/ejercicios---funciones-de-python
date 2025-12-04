def pedir_dinero():
    cantidad_dinero = float (input("digite la cantidad de dinero de su cuenta: "))
    return cantidad_dinero

def calcular_interes(cantidad_dinero):
    porcentaje = 0.05
    interes = cantidad_dinero * porcentaje
    total = cantidad_dinero + interes
    return total

def inprimir_mensaje(total):
    print ("el total a pagar (con 5 porciento de interes) es: ", total,"$")
    
#*************codigo principal**************
dinero = pedir_dinero()
total = calcular_interes(dinero)
mensaje = inprimir_mensaje (total)