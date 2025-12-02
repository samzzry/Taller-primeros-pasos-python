
def leer_cantidad():
    cantidad = int(input("Digite la cantidad de números para sumar: "))
    return cantidad
def leer_numero(i):
    numero = int(input("Digite el Número " + str(i+1) + ": "))
    return numero
def sumar_numeros(cantidad):
    suma = 0
    for i in range(cantidad):
        num = leer_numero(i)
        suma = suma + num
    return suma
def imprimir_suma(suma):
    print("La sumatoria total es: " + str(suma))
# codigo rincipal


cantidad = leer_cantidad()
resultado = sumar_numeros(cantidad)
imprimir_suma(resultado)