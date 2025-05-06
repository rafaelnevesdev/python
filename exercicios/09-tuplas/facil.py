# Fácil
tupla = (1, 2, 3)
try:
    tupla[0] = 10
except TypeError as e:
    print("Erro:", e)
