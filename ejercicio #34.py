def pedir_precio ():
    precio = float (input("digite el precio del articulo: "))
    return precio

def calcular_descuento(precio):
    des = 0.10
    descuento = precio * des
    total = precio - descuento
    return total
    
def imprimir_total(total):
    print ("el precio total a pagar es: ",total)
    
#********codigo principal************

precio = pedir_precio()
descuento = calcular_descuento(precio)
total = imprimir_total(descuento)