# Desafio 8: Empacotamento e desempacotamento

# Fácil: Use *resto para pegar elementos restantes de uma lista.
valores = [1, 2, 3, 4, 5]
primeiro, *resto = valores
print("Primeiro:", primeiro)
print("Resto:", resto)

# Médio: Separe primeiro e último nome de uma lista de nomes completos.
nomes = ["Ana Silva", "Bruno Souza", "Carla Dias"]
for nome_completo in nomes:
    partes = nome_completo.split()
    primeiro, *_, ultimo = partes
    print("Primeiro:", primeiro, "| Último:", ultimo)

# Difícil: Desempacote uma lista de dados mistos em variáveis nomeadas.
dados = ["João", 25, "joao@email.com", "99999-0000"]
nome, idade, email, telefone = dados
print(f"Nome: {nome}, Idade: {idade}, Email: {email}, Telefone: {telefone}")