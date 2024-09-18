#O código calcula e exibe a idade em meses, o aumento de 10% no salário e o novo salário, 
#além de exibir o nome, idade e salário do usuário.

nome = input('escreva seu nome: ')
idade = int(input('escreva sua idade: '))
salario = float(input('escreva sua salario: '))

meses= idade * 12
aumento = salario * 1.1
novoSalario= salario + aumento

print(f'sou {nome} tenho {idade} e o meu salario é {salario}')
print(f'seu aumento de 10% é {aumento} e o novo salario seria: {novoSalario:,.2f}')
print(f' e a sua idade em meses é: {meses}')