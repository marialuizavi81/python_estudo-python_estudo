while True:
    print("Conversor de Temperatura")
    print("1 - Celsius para Fahrenheit")
    print("2 - Fahrenheit para Celsius")
    print("3 - Sair")
    escolha = int(input("Escolha uma opção: "))

    match escolha:
        case 1:
            celsius = float(input("Escreva a temperatura em Celsius: "))
            fahrenheit = (celsius * 1.8) + 32
            print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}")
        case 2:
            fahrenheit = float(input("Escreva a temperatura em Fahrenheit: "))
            celsius = (fahrenheit - 32) / 1.8
            print(f"A temperatura em Celsius é: {celsius:.2f}")
        case 3:
            print("Saindo...")
            break
        case _:
            print("Opção inválida. Tente novamente.")
