def pedir_num ():
    num = int(input("digite el numero: "))
    return num

def calcular_raiz (num):
    raiz = num** 0.5
    return raiz

def imprimir_mensaje(raiz, num):
    print ("la raiz cuadrada de √",num, "es: ",raiz)
    
#***********zona de codigo**********

num = pedir_num()
calculo = calcular_raiz(num)
mensaje = imprimir_mensaje(calculo, num)