# Desafio 10: Imprecisão de ponto flutuante

from decimal import Decimal

# Fácil: Faça 0.1 + 0.7 com float e Decimal e compare.
print("Float:", 0.1 + 0.7)
print("Decimal:", Decimal("0.1") + Decimal("0.7"))

# Médio: Some valores monetários com float e Decimal e veja a diferença.
valores = [0.1, 0.2, 0.3]
print("Soma float:", sum(valores))
valores_decimal = [Decimal("0.1"), Decimal("0.2"), Decimal("0.3")]
print("Soma Decimal:", sum(valores_decimal))

# Difícil: Sistema de caixa simples com Decimal para somar valores e calcular troco.
total = Decimal("0.00")
precos = [Decimal("1.99"), Decimal("2.50"), Decimal("3.75")]
for preco in precos:
    total += preco
print("Total:", total)
pagamento = Decimal("10.00")
troco = pagamento - total
print("Troco:", troco)