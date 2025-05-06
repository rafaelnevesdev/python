# Difícil
listas = [[1, 2], [3, 4]]
copia_listas = [x.copy() for x in listas]
listas[0][0] = 99
print("Original:", listas)
print("Cópia:", copia_listas)