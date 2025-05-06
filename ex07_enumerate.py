# Desafio 7: enumerate()

# Fácil: Mostre os índices e elementos de uma lista usando enumerate().
nomes = ["Ana", "Bruno", "Carla"]
for i, nome in enumerate(nomes):
    print(i, nome)

# Médio: Crie um menu numerado com opções.
opcoes = ["Iniciar", "Configurações", "Sair"]
for i, opcao in enumerate(opcoes, 1):
    print(f"{i}. {opcao}")

# Difícil: Identifique os índices dos elementos com mais de 5 letras usando enumerate().
palavras = ["python", "java", "javascript", "go"]
for i, palavra in enumerate(palavras):
    if len(palavra) > 5:
        print(f"Índice {i}: {palavra}")