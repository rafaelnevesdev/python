# Desafio 20: for / range

# Fácil: Imprima os números pares de 0 a 20.
for n in range(0, 21, 2):
    print(n, end=" ")
print()

# Médio: Calcule a soma de todos os números de 1 a 100.
soma = sum(range(1, 101))
print("Soma de 1 a 100:", soma)

# Difícil: Gerador de tabuada de 1 a 10 usando for aninhado.
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print("-" * 15)