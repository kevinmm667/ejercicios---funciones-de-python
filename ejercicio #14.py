def pedir_medida ():
    pulgadas = float (input("digite la medida (pulgadas): "))
    return pulgadas

def convertir_medida (pulgadas):
    cm = 2.54
    convercion = pulgadas * cm
    return convercion

def mostrar_resultado (convercion):
    print ("la medida digitada (pulgadas) es a centimetros: ", convercion)

#*********codigo principal************

medida = pedir_medida()
pulg = convertir_medida (medida)
resultado = mostrar_resultado(pulg)