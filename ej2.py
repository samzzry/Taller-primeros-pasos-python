# 1. Función para mostrar el menú
def mostrar_menu():
    """Imprime las opciones del menú en la consola."""
    print("\n******** CÓDIGO PRINCIPAL DE PYTHON ********")
    print("Digite la letra 'A' para Actualizar Sistema")
    print("Digite la letra 'E' para Eliminar Catálogo")
    print("Digite la letra 'C' para Crear Productos")
    print("Digite la letra 'S' para salir del programa")
    print("--------------------------------------------")

# 2. Función para procesar la opción seleccionada
def procesar_opcion(letra):
    """
    Procesa la opción ingresada por el usuario.
    Retorna True si la opción es 'S' o 's' (salir), de lo contrario False.
    """
    letra = letra.upper() # Convertir a mayúsculas para simplificar la comparación

    if letra == 'A':
        print("\n--> Procesando: Actualizar Sistema...")
        # Aquí iría el código para actualizar el sistema
    elif letra == 'E':
        print("\n--> Procesando: Eliminar Catálogo...")
        # Aquí iría el código para eliminar el catálogo
    elif letra == 'C':
        print("\n--> Procesando: Crear Productos...")
        # Aquí iría el código para crear productos
    elif letra == 'S':
        print("\n--> Finalizó con éxito.")
        return True  # Indica que se debe salir del bucle
    else:
        print("\nSigue dentro del proceso del DO WHILE. Opción no válida. Intente de nuevo.")

    return False # Indica que se debe continuar en el bucle

# 3. Función principal que contiene el bucle de ejecución
def main():
    """
    Función principal que ejecuta el bucle de menú.
    Equivalente a la estructura Do-While con 'while True'.
    """
    salir = False
    
    while True:
        mostrar_menu()
        
        # Se solicita la entrada del usuario
        try:
            letra = str(input("Ingrese su opción: "))
        except EOFError:
             # Manejo de error si el input es interrumpido
            print("\nError de lectura de entrada. Saliendo...")
            break
        
        # Se procesa la opción y se verifica si se debe salir
        salir = procesar_opcion(letra)
        
        # El 'break' para salir del bucle se ejecuta si procesar_opcion retorna True
        if salir:
            break
            
    print("EL DO-WHILE ha finalizado.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
