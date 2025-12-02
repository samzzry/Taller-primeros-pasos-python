def pedir_numero():
    num = int(input("Digite un número: "))
    return num
def verificar_paridad(num):
    if num % 2 == 0:
        resultado = "El número es par"
    else:
        resultado = "El número es impar"
    return resultado
def imprimir_resultado(resultado):
    print(resultado)
# Programa rincipal
num = 1
while num != 0:
    num = pedir_numero()
    if num != 0:
        resultado = verificar_paridad(num)
        imprimir_resultado(resultado)
print("Finalizó el programa")