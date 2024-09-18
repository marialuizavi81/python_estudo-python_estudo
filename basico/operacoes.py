
'''O programa realiza e exibe a soma, subtração, multiplicação, 
exponenciação e divisão de dois números fornecidos pelo usuário.'''
#input dos valores
num = int(input('Escreva o primeiro número: '))
num2 = int(input('Escreva o segundo número: '))


print(f'Você forneceu os números: {num} e {num2}')

print(f'Soma: {num} + {num2} = {num + num2}')
print(f'Subtração: {num} - {num2} = {num - num2}')
print(f'Multiplicação: {num} * {num2} = {num * num2}')
print(f'Potência: {num} ** {num2} = {num ** num2}')
print(f'Divisão: {num} / {num2} = {num / num2:.2f}')
print(f'Resto da divisão: {num} % {num2} = {num % num2}')

media = (num + num2) / 2
print(f'Média: ({num} + {num2}) / 2 = {media:.2f}')