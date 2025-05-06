# Desafio 12: f-strings

# Fácil: Formate uma mensagem com nome e idade usando f-string.
nome = "Rafael"
idade = 30
print(f"Meu nome é {nome} e tenho {idade} anos.")

# Médio: Mostre o resultado de uma operação matemática dentro de uma f-string.
a = 5
b = 3
print(f"{a} + {b} = {a + b}")

# Difícil: Gere relatórios dinâmicos com f-strings, mostrando dados tabulados e formatados.
dados = [
    {"nome": "Ana", "idade": 28, "cidade": "SP"},
    {"nome": "Bruno", "idade": 34, "cidade": "RJ"},
    {"nome": "Carla", "idade": 22, "cidade": "BA"}
]
print(f"{'Nome':<10} {'Idade':<5} {'Cidade':<10}")
for pessoa in dados:
    print(f"{pessoa['nome']:<10} {pessoa['idade']:<5} {pessoa['cidade']:<10}")