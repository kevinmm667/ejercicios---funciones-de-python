def pedir_num1():
    num1 = int(input("digite su primer numero: "))
    return num1

def pedir_num2():
    num2 = int(input("digite su segundo numero: "))
    return num2

def sumar_num(num1, num2):
    suma = num1 + num2
    return suma

def mostra_resultado(suma):
    print ("total = ", suma)

#*********codigo principal*********************

num1 = pedir_num1()
num2 = pedir_num2()
suma = sumar_num(num1, num2)
total = mostra_resultado(suma)