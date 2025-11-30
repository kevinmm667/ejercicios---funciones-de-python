def pedir_baseMayor ():
    base_mayor = float (input("digite el valor de la base mayor: "))
    return base_mayor

def pedir_baseMenor():
    base_menor = float (input("digite el valor de l base menor: "))
    return base_menor

def pedir_altura():
    altura = float (input("digite el valor de la altura: "))
    return altura

def calcular_area(base_mayor, base_menor, altura):
    area = ((base_mayor + base_menor) /2) * altura
    return area

def mostrar_resultado (area):
    print ("el area del trapecio es: ", area)

#************codigo principal***************

base_mayor = pedir_baseMayor()
base_menor = pedir_baseMenor()
altura = pedir_altura()
area = calcular_area (base_mayor, base_menor, altura)
resultado_area = mostrar_resultado(area) 