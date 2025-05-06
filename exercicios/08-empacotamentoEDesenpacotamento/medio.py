# Médio
nomes_completos = ["João Silva", "Maria Oliveira"]
for nome in nomes_completos:
    primeiro, *_, ultimo = nome.split()
    print("Primeiro:", primeiro, "| Último:", ultimo)