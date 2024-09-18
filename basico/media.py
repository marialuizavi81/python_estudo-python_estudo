#código calcula e exibe a média de notas fornecidas pelo usuário.
#Ediz que esta reprovado ou recuperaçao.
nota1 = float(input(("escreva a primeira nota: ")))
nota2 = float(input(("escreva a primeira nota: ")))
nota3 = float(input(("escreva a primeira nota: ")))

media = (nota1 + nota2 + nota3)/3

if media >= 7:
    print(f"voce esta aprovado {media:,.2f}!!!")

elif media >= 4:
    print(f"voce esta na final {media:,.2f} cuidado nao.")

else:
    print(f"voce esta reprovado {media:,.2f}")