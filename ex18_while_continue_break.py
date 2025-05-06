# Desafio 18: while com continue e break

# Fácil: Peça nomes em loop até digitar 'sair'.
while True:
    nome = input("Digite um nome (ou 'sair' para encerrar): ")
    if nome.lower() == "sair":
        break
    print("Nome digitado:", nome)

# Médio: Pule nomes com menos de 3 letras usando continue.
while True:
    nome = input("Digite um nome (ou 'sair' para encerrar): ")
    if nome.lower() == "sair":
        break
    if len(nome) < 3:
        continue
    print("Nome válido:", nome)

# Difícil: Sistema de login com 3 tentativas, pulando tentativas vazias e encerrando ao acerto com break.
tentativas = 0
while tentativas < 3:
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    if not usuario or not senha:
        print("Usuário e senha não podem ser vazios.")
        continue
    if usuario == "admin" and senha == "1234":
        print("Login bem-sucedido!")
        break
    else:
        print("Login ou senha incorretos.")
        tentativas += 1
else:
    print("Número máximo de tentativas atingido.")