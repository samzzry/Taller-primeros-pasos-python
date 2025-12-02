
def solicitarnumeros():
    "
    Pide al usuario que digite un número y lo va retonar como entero
    "
    while True:
        try:
        
            num = int(input("Digite un número (0 para que todo el programa se acabe): "))
            return num
        except ValueError:
          
            print("Entrada no válida.")


def verificar(num):
    "
    Determina si el número dado es par o impar.
    "

    if num % 2 == 0:
        print(f"El número {num} es par.")
    else:
        print(f"El número {num} es impar.")


def main():
    "
    Función principal que el programa se ejecute
    "
   
    num = 1
    
   #codigo principal

  
    while num != 0:
        
        num = solicitarnumeros()
        
       
        if num != 0:
           
            verificar(num)
        
    print("el programa acabo.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()

