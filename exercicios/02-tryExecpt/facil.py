# Fácil
try:
    a = float(input("Digite o numerador: "))
    b = float(input("Digite o denominador: "))
    print("Resultado:", a / b)
except ZeroDivisionError:
    print("Não pode dividir por zero!")