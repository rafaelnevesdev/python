# Desafio 21: Variáveis

# Fácil: Crie variáveis para nome, idade e altura. Imprima uma frase com elas.
nome = "Rafael"
idade = 30
altura = 1.75
print(f"Meu nome é {nome}, tenho {idade} anos e {altura}m de altura.")

# Médio: Troque os valores de duas variáveis entre si (sem criar outra linha).
a = 10
b = 20
a, b = b, a
print("a:", a)
print("b:", b)

# Difícil: Sistema de cadastro de usuário que armazena múltiplas variáveis e exibe um resumo formatado.
usuario_nome = input("Nome: ")
usuario_idade = int(input("Idade: "))
usuario_email = input("Email: ")
usuario_cidade = input("Cidade: ")
print("\nResumo do cadastro:")
print(f"Nome: {usuario_nome}")
print(f"Idade: {usuario_idade}")
print(f"Email: {usuario_email}")
print(f"Cidade: {usuario_cidade}")