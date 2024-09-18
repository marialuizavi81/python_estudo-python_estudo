#O programa exibe a soma de um número atual com o anterior em uma sequência de 10 iterações, atualizando o número atual a cada passo.
x = 0
numeros_somados = 0
numeros_a = 0 
numero1 = 0 

while x < 10: 
    numero_anterior = numero1  
    numero1 = int(input("Escreva um número: "))
    numeros_a = numeros_a + numero1

    numeros_somados = numeros_somados + numeros_a
    x = x + 1

    print(f"A soma de {numero_anterior} + {numero1} é {numeros_a} adicionando para a soma dos numeros que no total é: {numeros_somados}")

print(f"O número somado de todos foi: {numeros_somados}")