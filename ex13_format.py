# Desafio 13: format()

# Fácil: Use .format() para exibir nome, idade e profissão em uma frase.
nome = "Rafael"
idade = 30
profissao = "Desenvolvedor"
print("Nome: {}, Idade: {}, Profissão: {}".format(nome, idade, profissao))

# Médio: Alinhe texto com .format() (esquerda, direita, centralizado).
print("{:<10}".format("esquerda"))
print("{:^10}".format("centro"))
print("{:>10}".format("direita"))

# Difícil: Crie uma tabela com cabeçalho e linhas formatadas com .format() e placeholders.
print("{:<10} | {:<5} | {:<10}".format("Nome", "Idade", "Cidade"))
print("-" * 30)
print("{:<10} | {:<5} | {:<10}".format("Ana", 28, "SP"))
print("{:<10} | {:<5} | {:<10}".format("Bruno", 34, "RJ"))
print("{:<10} | {:<5} | {:<10}".format("Carla", 22, "BA"))