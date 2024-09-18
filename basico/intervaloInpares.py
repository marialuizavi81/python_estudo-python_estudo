# calcula a soma dos números ímpares em um intervalo definido pelo usuário,
# assegurando que o valor inicial não seja maior que o valor final.
x = 0
soma = 0
inicial = int(input("escreva um valor inicial para tal:"))
final = int(input("escreva um valor final para tal:"))

while inicial > final:
    print("valor invalido, inicial nao pode ser maior que final")
    inicial = int(input("escreva um valor inicial para tal:"))
    final = int(input("escreva um valor final para tal:"))

for x in range(inicial,final+1,1):
     if x % 2 != 0:
        soma = soma + x
    
print(f"a soma dos numeros inpares no intervalo é:{soma}")