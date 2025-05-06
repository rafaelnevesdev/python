# Desafio 4: Tipos imutáveis

# Fácil: Tente alterar uma letra de uma string diretamente.
try:
    palavra = "python"
    # Isso vai gerar erro, pois strings são imutáveis
    palavra[0] = "P"
except TypeError as e:
    print("Erro:", e)

# Médio: Crie dois inteiros iguais, altere um, e comprove que são independentes.
a = 10
b = a
b = 20
print("a:", a)  # 10
print("b:", b)  # 20

# Difícil: Construa uma nova string trocando letras específicas sem alterar a original.
original = "banana"
nova = original.replace("a", "o")
print("Original:", original)
print("Nova:", nova)