def pedir_litros ():
    litros = float (input("escriba la cantidad de litros(Lt) para pasar a galones(gl): "))
    return litros

def convertir_litros(litros):
    galones = 0.264172
    convercion = litros * galones
    return convercion 

def mostrar_resultado (convercion):
    print ("los litros que escribio equivalen a: ",convercion, "galones")
    
#***********codigo principal***************

litros = pedir_litros()
convertir = convertir_litros(litros)
resultado = mostrar_resultado(convertir)
