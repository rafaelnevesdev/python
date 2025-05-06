# Desafio 17: if / elif / else

# Fácil: Classifique uma nota: <5 (ruim), 5-7 (ok), >7 (ótimo).
nota = float(input("Digite a nota: "))
if nota < 5:
    print("Ruim")
elif 5 <= nota <= 7:
    print("Ok")
else:
    print("Ótimo")

# Médio: Diga o tipo de número digitado: positivo, negativo ou zero.
num = float(input("Digite um número: "))
if num > 0:
    print("Positivo")
elif num < 0:
    print("Negativo")
else:
    print("Zero")

# Difícil: Sistema de recomendação com base em faixa etária e interesse do usuário.
idade = int(input("Idade: "))
interesse = input("Prefere filmes ou esportes? ").lower()
if idade < 12:
    print("Recomendação: Desenhos animados")
elif 12 <= idade < 18:
    if interesse == "filmes":
        print("Recomendação: Filmes de aventura")
    else:
        print("Recomendação: Esportes radicais")
else:
    if interesse == "filmes":
        print("Recomendação: Documentários")
    else:
        print("Recomendação: Esportes tradicionais")