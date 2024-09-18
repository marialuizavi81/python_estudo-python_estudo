#O programa calcula o custo de uma chamada telefônica com base no número de minutos
#aplicando tarifas diferenciadas para diferentes faixas de duração.
minutos = int(input("Escreva quantos minutos você passou: "))

if minutos <= 200:
    valor = minutos * 0.20
    
elif 201 <= minutos <= 400:
    valor = minutos * 0.18
    
else: 
    valor = minutos * 0.15

print(f"O valor que você vai pagar é R${valor:.2f}")