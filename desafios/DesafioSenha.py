#código pede ao usuário para criar uma senha e depois solicitar uma senha para acesso,
#permitindo até três tentativas antes de bloquear o acesso se a senha estiver incorreta.
senha = 0
x =1

senha = input("escreva uma senha para ser registrada: ")
novasenha = input("escreva a senha para entrar")

while x <= 3:
    if senha == novasenha: 
        print("acesso liberado, entre: ")
        break
    else: 
        print(f"acesso negado, voce esta na {x} tentativa, se ouver 3 tentativas erradas voce vai ser bloqueado: ")
        novasenha = input("escreva a senha para entrar")
        x+=1
    if x > 3: 
        print("voce esta bloqueado.")
        