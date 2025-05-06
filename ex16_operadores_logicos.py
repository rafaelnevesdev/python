# Desafio 16: Operadores lógicos

# Fácil: Verifique se uma pessoa pode entrar (idade > 18 e tem ingresso).
idade = int(input("Digite a idade: "))
tem_ingresso = input("Tem ingresso? (s/n): ").lower() == "s"
if idade > 18 and tem_ingresso:
    print("Pode entrar.")
else:
    print("Não pode entrar.")

# Médio: Peça login e senha e use and para validar.
login = input("Login: ")
senha = input("Senha: ")
if login == "admin" and senha == "1234":
    print("Acesso permitido.")
else:
    print("Acesso negado.")

# Difícil: Combine múltiplas condições com and, or e not em um sistema de acesso com níveis.
usuario = input("Usuário: ")
senha = input("Senha: ")
nivel = input("Nível (admin/user): ")
if (usuario == "admin" and senha == "1234" and nivel == "admin") or (usuario == "user" and senha == "abcd" and nivel == "user"):
    print("Acesso liberado para", nivel)
else:
    print("Acesso negado.")