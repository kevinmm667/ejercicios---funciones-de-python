def pedir_numero():
    num = int(input("digite un numero: "))
    return num

def verificar_num(num):
    if num%2 == 0:
        print ("el numero es par")
    else:
        print ("el numero es impar")
        
#codigo principal

numero = pedir_numero()
verificacion = verificar_num(numero)

        
    