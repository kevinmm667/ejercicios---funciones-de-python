def pedir_num1():
    num1 = int(input("digite el primer dato: "))
    return num1

def pedir_num2():
    num2 = int(input("digite el segundo dato: "))
    return num2

def procesar_dato(num1, num2):
    if num1 < num2:
        mensaje = "el valor "+ str(num1)+" es menor que "+ str(num2)
    elif num1 == num2:
        mensaje = "el valor "+ str(num1)+" es igual que "+ str(num2)
    else:
        mensaje = "el valor "+ str(num1)+" es mayor que "+ str(num2)
    return mensaje
    
def mostrar_mensaje(mensaje):
    print (mensaje)

#***************codigo principal******************

dato1 = pedir_num1()
dato2 = pedir_num2()
proceso = procesar_dato(dato1, dato2)
mostrar_mensaje (proceso)
