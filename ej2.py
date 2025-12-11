def mostrar_menu():
    print("Digite la letra 'A' para Actualizar Sistema")
    print("Digite la letra 'E' para Eliminar Catálogo")
    print("Digite la letra 'C' para Crear Productos")
    print("Digite la letra 'S' para salir del programa")
def leer_opcion():
    letra = str(input("Digite una opción: "))
    return letra
def procesar_opcion(letra):
    if letra == 'S' or letra == 's':
        return True
    else:
        print("Sigue dentro del proceso de do while\n")
        return False
# codigo principal
while True:
    mostrar_menu()
    opcion = leer_opcion()
    salir = procesar_opcion(opcion)
    if salir:
        print("Finalizó con éxito\n")
        break

print("do while ha finalizado\n")
