#utilizando match para soma, subtraçao, multplicaçao,divsisao,digitar novo numero e sair.
opicao = 1

n1 = float(input(" escreva um primeiro numero: "))
n2 = float(input(" escreva um segundo numero: "))

while opicao == 1:

    opera = int(input("somar = 1\n"
                    "subtraçao = 2\n"
                    "multiplicacao = 3\n"
                    "divisao = 4\n"
                    "para digitar novos numeros = 5\n"
                    "sair = 6\n"
                    "digite o numero da operação que deseja realizar: "))

    match opera:
        case 1:
            soma = n1 + n2
            print("---")
            print(f"A soma é: {soma}")
            print("---")
        case 2:
            subtra = n1 - n2
            print("---")
            print(f"A subtração é: {subtra}")
            print("---")
        case 3:
            mult = n1 * n2
            print("---")
            print(f"A multiplicação é: {mult}")
            print("---")
        case 4:
            div = n1 / n2
            print("---")
            print(f"A divisão é: {div}")
            print("---")
        case 5:
            print("---")
            n1 = float(input(" escreva um primeiro numero: "))
            n2 = float(input(" escreva um segundo numero: "))
            print("---")
        case 6:
            opcao = 0
        case _:
            print("---")
            print("Opção inválida. Tente novamente.")

print("Programa encerrado.")


