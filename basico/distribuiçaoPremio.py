'''O programa calcula e exibe a distribuição de um prêmio 
entre três ganhadores com diferentes porcentagens.'''

valor = float(input('qual será o premio a ser destribuido: '))

primeiroGanhador = 0.46 * valor 
segundoGanhador = 0.32 * valor 
terceiroGanhador = 0.22 * valor 
 
print(f'O valor de cada ganhador seria:\n'
      f'O primeiro ganhador recebe: {primeiroGanhador}\n'
      f'O segundo ganhador recebe: {segundoGanhador}\n'
      f'O terceiro ganhador recebe: {terceiroGanhador}')
