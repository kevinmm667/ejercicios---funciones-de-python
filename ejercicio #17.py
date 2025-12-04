#zona de funciones
def pedir_libras():
    libras = float(input("ingrese la cantidad de libras (lb): "))
    return libras

def convertir_libras(libras):
    kl = 0.4536
    libras_kg = libras * kl
    return libras_kg

def mostrar_mensaje (libras_kg):
    print ("la cantidad de libras ingresadas a kilogramos son: ", libras_kg,"kg")
    
#*************codigo principal****************

libras = pedir_libras()
kilogramos = convertir_libras(libras)
resultado = mostrar_mensaje(kilogramos)