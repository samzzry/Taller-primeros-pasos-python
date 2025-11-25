
def es_positivo(numero):
    """Retorna True si el número es mayor que cero."""
    return numero > 0


def es_negativo(numero):
    """Retorna True si el número es menor que cero."""
    return numero < 0


def es_neutro(numero):
    """Retorna True si el número es igual a cero."""
    return numero == 0


def identificar_signo():
    """
    Solicita un número al usuario y determina si es positivo,
    negativo o neutro usando las tres funciones definidas.
    """
    try:
       
        entrada = input("Por favor, introduce un número: ")
        numero = float(entrada)
        if es_positivo(numero):
            print(f"El número {numero} es **POSITIVO** **⬆️**.")
        elif es_negativo(numero):
            print(f"El número {numero} es **NEGATIVO** **⬇️**.")
        elif es_neutro(numero):
            print(f"El número {numero} es **NEUTRO** (Cero) **0️⃣**.")
        
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número real.")


if __name__ == "__main__":
    identificar_signo()
