def pedir_num():
    num = int(input("digite un numero: "))
    return num

def cuadrado_num(num):
    cuadrado = num**2
    return cuadrado

def mostra_resultado(cuadrado):
    print ("total = ", cuadrado)

#*********codigo principal*********************

num = pedir_num()
cuadrado = cuadrado_num(num)
total = mostra_resultado(cuadrado)