from decimal import Decimal

# Médio
valores = [0.1, 0.2, 0.3]
soma_float = sum(valores)
soma_decimal = sum(Decimal(str(v)) for v in valores)
print("Soma float:", soma_float)
print("Soma decimal:", soma_decimal)
