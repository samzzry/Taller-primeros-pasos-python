def numero_mes():
    num = int(input("Digite un número del 1 al 12: "))
    return num
def obtener (num):
    match num:
        case 1:
            mes = "Enero"
        case 2:
            mes = "Febrero"
        case 3:
            mes = "Marzo"
        case 4:
            mes = "Abril"
        case 5:
            mes = "Mayo"
        case 6:
            mes = "Junio"
        case 7:
            mes = "Julio"
        case 8:
            mes = "Agosto"
        case 9:
            mes = "Septiembre"
        case 10:
            mes = "Octubre"
        case 11:
            mes = "Noviembre"
        case 12:
            mes = "Diciembre"
        case _:
            mes = "Número fuera de rango"
    return mes

#codigo orincipal
def imprimmes(mes):
    print(mes)
numero = numero_mes()
mes = obtener(numero)

imprimmes(mes)
