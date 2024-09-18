'''Fac ̧a um programa que leia varios n  ́ umeros, calcule e mostre:
(a) A soma dos numeros digitados  ́
(b) A quantidade de numeros digitados  ́
(c) A media dos n  ́ umeros digitados  ́
(d) O maior numero digitado  ́
(e) O menor numero digitado  ́
(f) A media dos n  ́ umeros pares  ́'''

x= 1
soma = 0 
maior = 0
menor = 8364548
pares = 0 
numerosPares = 0

quantidadeNumeros = int(input("escreva a quantidade de numeros que voce quer: "))

while x <= quantidadeNumeros:
    numeros = int(input(f"{x}° escreva os numeros: "))

    #A soma dos numeros digitados  
    soma = soma + numeros

    #A quantidade de numeros digitados
    
    #A media dos n  numeros digitados  
    media = soma / quantidadeNumeros
    
    #O maior numero digitado  
    if maior < numeros: 
        maior = numeros 
    
    #O menor numero digitado  
    if numeros < menor: 
        menor = numeros  
    
    #A media dos numeros pares
    if numeros %2 == 0:
        pares +=1
        numerosPares = numerosPares + numeros
        mediaPares= numerosPares / pares
        
    x+=1

print (f"a soma dos numeros foi {soma}")
print()
print (f"a quantidade de numeros digitados é: {quantidadeNumeros}")
print()
print(f"a media dos numeros digitado é {media}")
print()
print(f"o maior numero foi {maior}")
print()
print(f"o menor numero foi {menor}")
print()
print(f"a quantidade de numeros pares digitado é: {pares}\n"
        f"a soma de todos os numeros pares é {numerosPares}\n"
        f"a media dos numeros pares é: {media}")