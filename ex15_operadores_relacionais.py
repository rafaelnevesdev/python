# Desafio 15: Operadores relacionais

# Fácil: Peça dois números e diga qual é maior, menor ou se são iguais.
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
if a > b:
    print("O primeiro é maior.")
elif a < b:
    print("O segundo é maior.")
else:
    print("São iguais.")

# Médio: Verifique se a idade digitada é maior que 18.
idade = int(input("Digite sua idade: "))
if idade > 18:
    print("Maior de idade.")
else:
    print("Menor de idade.")

# Difícil: Sistema que verifica se a média de um aluno permite sua aprovação com base em regras.
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
media = (nota1 + nota2) / 2
if media >= 7:
    print("Aprovado!")
elif 5 <= media < 7:
    print("Recuperação.")
else:
    print("Reprovado.")