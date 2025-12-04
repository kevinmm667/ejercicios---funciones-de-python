def pedir_num1():
    num1 = int(input("digite su primer numero: "))
    return num1

def pedir_num2():
    num2 = int(input("digite su segundo numero: "))
    return num2

def residuo_num(num1, num2):
    residuo = num1 % num2
    return residuo

def mostra_resultado(residuo):
    print ("total(residuo) = ", residuo)

#*********codigo principal*********************

num1 = pedir_num1()
num2 = pedir_num2()
residuo = residuo_num(num1, num2)
total = mostra_resultado(residuo)