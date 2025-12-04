def pedir_radio ():
    radio = float(input("digite el radio del circulo: "))
    return radio

def calcular_circunferencia(radio):
    pi = 3.1415
    circunferencia = (radio * 2) * pi
    return circunferencia

def mostrar_mensaje(circunferncia):
    print ("la circunferencia del circulo es: ", circunferncia)
    
#***********codigo principal*****************
radio = pedir_radio()
procedimiento = calcular_circunferencia(radio)
mensaje = mostrar_mensaje(procedimiento)