#utilizando o if-else
velocidade = int(input('Escreva a sua velocidade: '))

if velocidade > 80: 
    multa = (velocidade-80)*5
    print(f'Você foi multado em R${multa} reais')
else: 
    print(f'Tranquilo')