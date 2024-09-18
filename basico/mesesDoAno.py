#meses do ano
mes_numero = int( input("escreva o numero do mes: "))

while mes_numero <1 or mes_numero >12:
    print("Valor invalido")
    print("escreva um novo numero.")
    mes_numero = int( input("escreva o numero do mes: "))
    
    
match  mes_numero:
    case 1:
        print("janeiro")
    case 2:
        print("fevereiro")
    case 3:
        print("março")
    case 4:
        print("abrio")
    case 5:
        print("maio")
    case 6:
        print("junho")
    case 7:
        print("julho")
    case 8:
        print("agosto")
    case 9:
        print("setembro")
    case 10:
        print("outubro")
    case 11:
        print("novenbro")
    case 12:
        print("dezeenbro")