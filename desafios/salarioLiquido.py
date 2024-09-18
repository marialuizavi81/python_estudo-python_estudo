# Programa para calcular o salário líquido

valor_hora = float(input("Digite o valor da sua hora: R$ "))
quantidade_horas = float(input("Digite a quantidade de horas trabalhadas no mês: "))


salario_bruto = valor_hora * quantidade_horas


if salario_bruto <= 900:
    desconto_ir = 0
    porcentagem_ir = "Isento"
    
elif salario_bruto >= 901 and salario_bruto <= 1500:
    desconto_ir = salario_bruto * 0.05
    porcentagem_ir = "5%"
    
elif salario_bruto <= 2500:
    desconto_ir = salario_bruto * 0.1
    porcentagem_ir = "10%"
    
else:
    desconto_ir = salario_bruto * 0.2
    porcentagem_ir = "20%"

desconto_inss = salario_bruto * 0.1

fgts = salario_bruto * 0.11

total_descontos = desconto_ir + desconto_inss

salario_liquido = salario_bruto - total_descontos


print("\nInformações do salário:")
print(f"Salário bruto (R$ {valor_hora:.2f} * {quantidade_horas:.2f}h): R$ {salario_bruto:.2f}")
print(f"(–) IR ({porcentagem_ir}): R$ {desconto_ir:.2f}")
print(f"(–) INSS (10%): R$ {desconto_inss:.2f}")
print(f"FGTS (11%): R$ {fgts:.2f}")
print(f"Total de descontos: R$ {total_descontos:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")