# Desafio 14: Operadores aritméticos

# Fácil: Faça as 4 operações básicas com dois números.
x = 8
y = 2
print("Soma:", x + y)
print("Subtração:", x - y)
print("Multiplicação:", x * y)
print("Divisão:", x / y)

# Médio: Calcule o quadrado, cubo e raiz quadrada de um número.
num = 9
print("Quadrado:", num ** 2)
print("Cubo:", num ** 3)
print("Raiz quadrada:", num ** 0.5)

# Difícil: Calculadora com escolha da operação via input do usuário.
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
op = input("Escolha a operação (+, -, *, /): ")
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b != 0:
        print(a / b)
    else:
        print("Divisão por zero!")
else:
    print("Operação inválida.")