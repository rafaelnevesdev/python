# Desafio 9: Tuplas

# Fácil: Crie uma tupla e tente modificar um valor (deve falhar).
try:
    t = (1, 2, 3)
    t[0] = 99
except TypeError as e:
    print("Erro:", e)

# Médio: Converta uma lista em tupla e depois de volta para lista.
lista = [4, 5, 6]
tupla = tuple(lista)
lista2 = list(tupla)
print("Lista:", lista)
print("Tupla:", tupla)
print("Lista2:", lista2)

# Difícil: Use tuplas para armazenar coordenadas de um mapa e acesse os valores de forma dinâmica.
coordenadas = [(0, 0), (1, 2), (3, 4)]
for i, (x, y) in enumerate(coordenadas):
    print(f"Ponto {i}: x={x}, y={y}")