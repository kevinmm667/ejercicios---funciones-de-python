def pedir_num1():
    num1 = int(input("digite su primer numero: "))
    return num1

def pedir_num2():
    num2 = int(input("digite su segundo numero: "))
    return num2

def resta_num(num1, num2):
    resta = num1 - num2
    return resta

def mostra_resultado(resta):
    print ("total = ", resta)

#*********codigo principal*********************

num1 = pedir_num1()
num2 = pedir_num2()
resta = resta_num(num1, num2)
total = mostra_resultado(resta)