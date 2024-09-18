''' dados os valores de horarios abaixo,decifre a logica e faça um codigo para executar
entrada1 3:45
entrada2 14:20 
saida 6:05'''
horastotais = 0
minutostotais = 0

hora1 = int(input("escreva a hora: "))
minutos1 = int(input("escreva a minutos: "))

hora2 = int(input("escreva a hora: "))
minutos2 = int(input("escreva a minutos: "))

if int(hora1 and hora2) <= 24 and int(minutos1 and minutos2) <= 60:

        horastotais = (hora2 + hora1) %12

        minutostotais = (minutos2 + minutos1)

        if minutostotais > 60:
            horastotais = horastotais + 1
            minutostotais = minutostotais - 60

        print(f"O horário total é: {horastotais:02d}:{minutostotais:02d}")
else:
    print("erro: o horario colocado nao corresponde a 24h e 60m")