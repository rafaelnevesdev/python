# Desafio 5: Fatiamento de strings

# Fácil: Mostre os 3 primeiros e os 3 últimos caracteres de uma palavra.
palavra = "programacao"
print("3 primeiros:", palavra[:3])
print("3 últimos:", palavra[-3:])

# Médio: Inverta uma string usando slicing [::-1].
invertida = palavra[::-1]
print("Invertida:", invertida)

# Difícil: Crie uma nova string com apenas as letras nas posições pares.
pares = palavra[::2]
print("Letras nas posições pares:", pares)