#código calcula e exibe o valor a ser pago com base na quantidade de litros 
#e no tipo de combustível (etanol ou gasolina) inserido pelo usuário.
litros = float(input(" escreva a quantidade de litros que voce colocou: "))
escolha = input("voce colocou E-tanol(escreva E) ou Gasolina?(escreva G): ")

Ga = 5.80
et = 4.90
valor = 0

if escolha == "G" or escolha == "g":
    valor = Ga * litros
    print(f" voce vai pagar {valor:,.2f} com {escolha}")

elif escolha == "E" or escolha == "e":
    valor = et * litros
    print(f" voce vai pagar {valor:,.2f} com {escolha}")

else:
    print("combustivel invalido")
