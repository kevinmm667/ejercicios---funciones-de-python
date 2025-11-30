def pedir_dato ():
    g_celsius = float (input("dogite los grados celsius: "))
    return g_celsius

def convertir_grados (g_celsius):
    fahrenheit = (g_celsius * 9/5) + 32
    return fahrenheit

def mostrar_convercion (fahrenheit):
    print ("los grados celsius a fahrenheit son: ", fahrenheit,"°F")
    
#codigo principal:

datos = pedir_dato()
convercion = convertir_grados (datos)
resultado = mostrar_convercion(convercion)    
    