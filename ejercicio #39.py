def pedir_num1():
    num1 = int (input("digite un numero: "))
    return num1

def pedir_num2():
    num2 = int (input("digite el segundo numero: "))
    return num2

def procesar_datos(num1, num2):
    promedio = (num1 + num2)/2
    return promedio

def mostrar_mensaje(promedio):
    print ("el promedio es: ", promedio)

#**************codigo principal**************

num1 = pedir_num1()
num2 = pedir_num2()
mensaje = procesar_datos(num1, num2)
promedio = mostrar_mensaje(mensaje)