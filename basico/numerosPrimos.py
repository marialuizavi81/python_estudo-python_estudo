#programa verifica se um número inteiro fornecido pelo usuário é primo.
def primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


numero = int(input("Digite um número inteiro maior que 1: "))

if primo(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")