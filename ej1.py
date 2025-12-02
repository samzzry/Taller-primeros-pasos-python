
def definir_numero():
    numero = int(input("Digite un número: "))
    return numero
def verificar_numero(numero):
    if numero > 0:
        resultado = "El número es Positivo."
    elif numero == 0:
        resultado = "El número es Neutro."
    else:
        resultado = "El número es Negativo."
    return resultado

def imprimir_datos(numero):
    print("Número ingresado:", numero)

def imprimir_resultado(resultado):
    print(resultado)
# Programa principal
numero = definir_numero()
resultado = verificar_numero(numero)
imprimir_datos(numero)
imprimir_resultado(resultado)