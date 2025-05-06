# Desafio 6: Listas (mutáveis e imutáveis)

# Fácil: Altere um elemento da lista e mostre o antes e depois.
lista = [1, 2, 3, 4]
print("Antes:", lista)
lista[2] = 99
print("Depois:", lista)

# Médio: Copie uma lista com .copy(), altere a original e comprove que a cópia não muda.
original = [10, 20, 30]
copia = original.copy()
original[0] = 99
print("Original:", original)
print("Cópia:", copia)

# Difícil: Crie uma lista de listas e altere um valor interno com cuidado para não alterar as cópias.
listas = [[1, 2], [3, 4]]
import copy
listas_copia = copy.deepcopy(listas)
listas[0][0] = 100
print("Listas:", listas)
print("Listas cópia:", listas_copia)