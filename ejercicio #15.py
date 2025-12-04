#zona de funciones
def pedir_base():
    base = int(input("digite el valor de la base del paralelogramo: "))
    return base

def pedir_altura():
    altura = int(input("digite el valor de la altura del paralelogramo: "))
    return altura

def calcular_area (base, altura):
    area = base * altura
    return area

def mostrar_resultado(area):
    print ("el area del paralelogramo es: ", area)
    
#*************codigo principal*************

base = pedir_altura()
altura = pedir_altura()
area = calcular_area(base,altura)
resultado = mostrar_resultado(area)