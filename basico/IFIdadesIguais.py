'''O programa compara as idades de duas pessoas e exibe se elas são iguais,
se uma é maior ou menor que a outra,
e verifica se os nomes são iguais.'''

print("aqui vamos ver se voce é mais velho,mais novo ou tem a idade igual a do seu amigo")

nome1 = (input('escreva seu nome: '))
idade1 = int(input('escreva a primeira idade: '))

nome2 = (input("escreva o nome do amigo: "))
idade2 = int(input('escreva a primeira idade: '))

if idade1 == idade2 :
    print('{} com {} e {} com  {}'.format(nome1,idade1,nome2,idade2) +' suas idades sao iguais')

if idade1 < idade2: 
     print('{} com {} a idade é menor que {} que tem {}'.format(nome1,idade1,nome2,idade2))

if idade1 > idade2 : 
     print('{} com {} a idade é maior que {} que tem   {}'.format(nome1,idade1,nome2,idade2))

if nome1 == nome2 : 
    print('seus nomes são iguais kkkk falta de criatividade' )
