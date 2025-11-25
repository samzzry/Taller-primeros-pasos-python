
def solicitar_numero():
    """
    Pide al usuario que digite un número y lo retorna como entero.
    Maneja posibles errores de entrada (como ingresar texto).
    """
    while True:
        try:
            # Pide el número al usuario
            numero = int(input("Digite un número (0 para finalizar): "))
            return numero
        except ValueError:
            # Maneja el caso en que el usuario no ingrese un número válido
            print("Entrada no válida. Por favor, ingrese un valor numérico.")


def verificar_paridad(num):
    """
    Determina si el número dado es par o impar (asumiendo que num != 0).
    """

    if num % 2 == 0:
        print(f"El número {num} es PAR.")
    else:
        print(f"El número {num} es IMPAR.")


def main():
    """
    Función principal que ejecuta el programa.
    Contiene el bucle 'while' que se ejecuta mientras el número sea diferente de cero.
    """
   
    num = 1
    
    print("******** CÓDIGO PRINCIPAL DE PYTHON ********")

  
    while num != 0:
        
        num = solicitar_numero()
        
       
        if num != 0:
           
            verificar_paridad(num)
        
    print("\nFinalizó el programa.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
