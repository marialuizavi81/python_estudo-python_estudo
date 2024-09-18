'''O programa calcula e exibe o desconto, o valor com desconto,
o valor parcelado em 3 vezes, 
e as comissões do vendedor para ambos os casos 
(com desconto e parcelado).'''

valor = float(input('qual o valor pago?: '))
Desconto = 0.1 * valor
valorComDesconto =  valor - Desconto

valorParcelado = valor / 3
comissaoDoVendedor =   0.05 * valorComDesconto
comissaoParcelado = 0.05 * valorParcelado


print(str(Desconto) + ' o desconto')
print(str(valorComDesconto) + ' valor com o desconto')
print(str(valorParcelado) + ' valor parcelado em 3 vezes sem juros')
print(str(comissaoDoVendedor) + ' valor da comissao do vendedor com o desconto')
print(str(comissaoParcelado) + ' valor da comissao do vendedor parcelado')