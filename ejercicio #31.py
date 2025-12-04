def pedir_horas():
    horas = float (input("ingrese la cantidad de horas para pasar a minutos: "))
    return horas

def pasar_min(horas):
    minutos = horas * 60
    return minutos

def mostrar_mensaje (minutos,horas):
    print (horas," son: ", minutos, " minutos")
    
#**********codigo principal***************

horas = pedir_horas()
min = pasar_min(horas)
mensaje = mostrar_mensaje(min, horas)