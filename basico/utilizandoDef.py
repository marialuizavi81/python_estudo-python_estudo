#programa coleta e armazena informações de vários usuários e, em seguida, exibe essas informações formatadas.
def coletar_informacoes():
    nome = input("Olá! Por favor, digite seu nome: ")
    idade = int(input("Quantos anos você tem? "))
    grana = float(input("Quanto dinheiro você tem (em reais)? "))
    return nome, idade, grana

def exibir_informacoes(nome, idade, grana):
    mensagem = (f'Olá, {nome}! Você tem {idade} anos e possui R${grana:.2f}. '
                f'É sempre bom saber como está sua situação financeira!')
    print(mensagem)

# Lista para armazenar as informações dos usuários
usuarios = []

# Coleta informações e armazena na lista
for _ in range(3):  # Altere o número para quantos usuários você deseja coletar
    nome, idade, grana = coletar_informacoes()
    usuarios.append({'nome': nome, 'idade': idade, 'grana': grana})

# Exibe as informações coletadas
for usuario in usuarios:
    exibir_informacoes(usuario['nome'], usuario['idade'], usuario['grana'])
