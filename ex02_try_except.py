# Desafio 2: try e except

# Fácil: Peça dois números e divida. Trate divisão por zero.
try:
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    resultado = a / b
    print("Resultado:", resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")

# Médio: Converta uma entrada para int e trate erro caso não seja número.
try:
    valor = int(input("Digite um número inteiro: "))
    print("Você digitou:", valor)
except ValueError:
    print("Erro: Isso não é um número inteiro.")

# Difícil: Valide uma senha numérica com try/except e número máximo de tentativas.
tentativas = 0
max_tentativas = 3
senha_correta = "1234"
while tentativas < max_tentativas:
    try:
        senha = input("Digite a senha numérica: ")
        if not senha.isdigit():
            raise ValueError("A senha deve ser numérica.")
        if senha == senha_correta:
            print("Acesso permitido!")
            break
        else:
            print("Senha incorreta.")
    except ValueError as e:
        print("Erro:", e)
    tentativas += 1
else:
    print("Número máximo de tentativas atingido.")