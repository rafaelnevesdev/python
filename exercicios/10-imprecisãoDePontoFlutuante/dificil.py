from decimal import Decimal

# Difícil
caixa = Decimal('0.00')
while True:
    valor = input("Digite o valor do item (ou 'fim'): ")
    if valor == 'fim':
        break
    caixa += Decimal(valor)
print("Total:", caixa)
pagamento = Decimal(input("Pagamento: "))
print("Troco:", pagamento - caixa)
