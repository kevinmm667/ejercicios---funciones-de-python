def pedir_medidas ():
    km = float (input("ingrese la distancia en kilomtros: "))
    return km

def calcular_km (km):
    millas = 0.621371
    calculo = km * millas
    return calculo

def mostrar_resultado (calculo):
    print ("los kilometros ingresados a millas son: ", calculo)

#*************codigo principal**************

km = pedir_medidas()
calculo = calcular_km(km)
millas = mostrar_resultado(calculo)