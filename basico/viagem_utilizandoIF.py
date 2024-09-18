#calcula o custo de uma viagem com base na distância percorrida, 
#aplicando uma tarifa diferente para distâncias de até 200 km e para distâncias superiores a isso.
distancia = float(input("Informe a distância: "))

if distancia <= 200:
    valor = distancia * 0.5
else: 
    valor = distancia * 0.45

print(f"O valor que você vai pagar é: {valor:.2f}")
