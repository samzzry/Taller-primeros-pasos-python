
def solicitar_cantidad():
    """
    Pide al usuario la cantidad total de números que desea sumar.
    Retorna la cantidad como un entero.
    """
    while True:
        try:
           
            cantidad = int(input("Digite la cantidad de números para sumar: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa. Intente de nuevo.")
                continue
            return cantidad
        except ValueError:
          
            print("Entrada no válida. Por favor, ingrese un número entero positivo.")


def solicitar_numero_y_sumar(suma_actual, indice):
    """
    Pide un número al usuario, lo suma a la suma_actual y retorna la nueva suma.
    El 'indice' se usa para el mensaje al usuario (ej: Número 1, Número 2).
    """
    while True:
        try:
         
            prompt = f"Digite el Número {indice}: "
            numero = int(input(prompt))
            
          
            return suma_actual + numero
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")


def main():
    """
    Función principal que ejecuta el programa de cálculo de sumatoria usando un bucle 'for'.
    """
    print("******** CÓDIGO PRINCIPAL DE PYTHON ********")
    
   
    cantidad_a_sumar = solicitar_cantidad()
    
  
    suma = 0
    
 
    if cantidad_a_sumar > 0:
        for i in range(cantidad_a_sumar):
          
            suma = solicitar_numero_y_sumar(suma, i + 1)
        
        
        print(f"\nLa sumatoria total es: {suma}")
    else:
        print("\nNo se ingresaron números para sumar. La sumatoria es 0.")


if __name__ == "__main__":
    main()
