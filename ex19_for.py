# Desafio 19: for

# Fácil: Percorra uma lista de números e imprima o dobro de cada um.
numeros = [1, 2, 3, 4, 5]
for n in numeros:
    print("Dobro:", n * 2)

# Médio: Conte quantos nomes possuem mais de 5 letras.
nomes = ["Ana", "Bruno", "Carla", "Fernanda", "João"]
contador = 0
for nome in nomes:
    if len(nome) > 5:
        contador += 1
print("Nomes com mais de 5 letras:", contador)

# Difícil: Gere uma lista com os quadrados dos números pares entre 1 e 20.
quadrados_pares = [n ** 2 for n in range(1, 21) if n % 2 == 0]
print("Quadrados dos pares:", quadrados_pares)