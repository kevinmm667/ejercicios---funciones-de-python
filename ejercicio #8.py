def pedir_dolar ():
    dolar = float(input("ingrese la cantidad de dinero (USD): "))
    return dolar

def pedir_tasa():
    T_cambio = float (input("ingrese la tasa de cambio: "))
    return T_cambio

def convertir_dolar(dolar, T_cambio):
    Euros = dolar * T_cambio
    return Euros

def mostrar_convercion(euros):
    print ("los dolares (USD) ingresados a euros son: ", euros)

#***********codigo principal*****************

dolar = pedir_dolar()
T_cambio = pedir_tasa()
convercion = convertir_dolar(dolar, T_cambio)
resultado = mostrar_convercion (convercion) 
