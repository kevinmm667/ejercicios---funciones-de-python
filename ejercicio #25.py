def pedir_num1():
    num1 = int(input("digite su primer numero: "))
    return num1

def pedir_num2():
    num2 = int(input("digite su segundo numero: "))
    return num2

def div_num(num1, num2):
    div = num1 / num2
    return div

def mostra_resultado(div):
    print ("total = ", div)

#*********codigo principal*********************

num1 = pedir_num1()
num2 = pedir_num2()
division = div_num(num1, num2)
total = mostra_resultado(division)