def pedir_num1():
    num1 = int(input("digite su primer numero: "))
    return num1

def pedir_num2():
    num2 = int(input("digite su segundo numero: "))
    return num2

def mult_num(num1, num2):
    mult = num1 * num2
    return mult

def mostra_resultado(mult):
    print ("total = ", mult)

#*********codigo principal*********************

num1 = pedir_num1()
num2 = pedir_num2()
mult = mult_num(num1, num2)
total = mostra_resultado(mult)