#************zona de funciones***********

def pedir_medidas():
    altura = float(input("ingrese el valor de la altura: ")) 
    base = float (input("ingrese el valor de la base: "))
    return altura, base

def calcular_area(altura, base):
    area = (altura * base / 2)
    return area

def mostrar_resultado(area):
    print ("el area del triangulo es:", area)

#***************zona de codigo principal**************     
    
altura,base = pedir_medidas()
resultado = calcular_area(altura , base)
mostrar_resultado (resultado)

  

    