
def solicitar_cantidad():
    """
    Pide al usuario la cantidad total de números que desea sumar y maneja errores.
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


def calcular_sumatoria(cantidad):
    """
    Recibe la cantidad de números, los solicita en un bucle 'for'
    y calcula la sumatoria total.
    Retorna la suma total.
    """

    suma = 0
    
   
    for i in range(cantidad):
        while True:
            try:
               
                prompt = f"Digite el Número {i+1}: "
                numero = int(input(prompt))
                break 
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")
                
      
        suma += numero
        
    return suma


def main():
    """
    Función principal que ejecuta el programa de cálculo de sumatoria usando 'for'.
    """
    print("******** CÓDIGO PRINCIPAL DE PYTHON ********")
    
  
    cantidad_a_sumar = solicitar_cantidad()
    
   
    if cantidad_a_sumar > 0:
        sumatoria_total = calcular_sumatoria(cantidad_a_sumar)
        
      
        print(f"\nLa sumatoria total es: {sumatoria_total}")
    else:
        print("\nNo se ingresaron números para sumar. La sumatoria es 0.")


if __name__ == "__main__":
    main()
