def pedir_datos():
    num1 = int (input("digite el primer numero: "))
    return num1

def pedir_dato2():
    num2 = int (input("digite el segundo numero: "))
    return num2

def procesar_datos(num1, num2):
    P = num1 / num2
    if P %2==0:
        mensaje = "es multiplo de "
    else:
        mensaje = "no es multiplo de "
        return mensaje
    
def imprimir_mensaje(num1, num2, mensaje):
    print ("el numero"+ str (num2), mensaje , "de "+ str(num1))
    

#***************codigo principal***********************
dato1 = pedir_datos()
dato2 = pedir_dato2()
proceso = procesar_datos(dato1, dato2)
mensaje = imprimir_mensaje (proceso, dato1, dato2)
