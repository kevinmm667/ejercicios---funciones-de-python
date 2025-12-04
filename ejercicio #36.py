def pedir_dato1():
    num1 = int (input("ingrese el numero dividendo: "))
    return num1

def pedir_dato2():
    num2 = int (input("ingrese el numero divisor: "))
    return num2

def procesar_datos(num1, num2):
    division = num1 / num2
    return division

def mostrar_resultado(division):
    print ("el cociente de la division es: ", division)
    
#***********codigo principal*****************

dato1 = pedir_dato1()
dato2 = pedir_dato2()
div = procesar_datos(dato1, dato2)
total = mostrar_resultado (div)