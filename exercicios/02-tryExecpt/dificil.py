# Difícil
tentativas = 3
while tentativas > 0:
    try:
        senha = int(input("Digite a senha numérica: "))
        if senha == 1234:
            print("Acesso concedido.")
            break
        else:
            print("Senha incorreta.")
            tentativas -= 1
    except ValueError:
        print("Senha deve ser numérica.")
else:
    print("Número máximo de tentativas atingido.")