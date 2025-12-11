
def defi():
    num = int(input("Digite un número: "))
    return num
def verificar_num(num):
    if num > 0:
        resultado = "El número es Positivo."
    elif num == 0:
        resultado = "El número es Neutro."
    else:
        resultado = "El número es Negativo."
    return resultado
def imprimir_datos(num):
    print("Número ingresado:", num)
def imprimir_resultado(resultado):
    print(resultado)
# Programa incipal
num = defi()
resultado = verificar_num(num)
imprimir_datos(num)
imprimir_resultado(resultado)
