#O código compara a quantidade de gols de dois times e imprime o nome do time vencedor ou informa um empate, dependendo dos gols registrados.
time1 = input("Digite o nome do primeiro time: ")
gols_time1 = int(input("Digite a quantidade de gols do primeiro time: "))

time2 = input("Digite o nome do segundo time: ")
gols_time2 = int(input("Digite a quantidade de gols do segundo time: "))


if gols_time1 > gols_time2:
    print(f"O time {time1} venceu com {gols_time1} gols.")
elif gols_time2 > gols_time1:
    print(f"O time {time2} venceu com {gols_time2} gols.")
else:
    print("O jogo terminou empatado.")
