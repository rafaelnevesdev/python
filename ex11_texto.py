# Desafio 11: Trabalhando com texto (split, join, strip)

# Fácil: Separe uma frase em palavras e mostre cada uma em uma linha.
frase = "Python é divertido de aprender"
palavras = frase.split()
for palavra in palavras:
    print(palavra)

# Médio: Peça uma lista de palavras separadas por vírgula, limpe e una com '-'.
entrada = "  casa, carro ,  rua,sol "
palavras = [p.strip() for p in entrada.split(",")]
resultado = "-".join(palavras)
print("Resultado:", resultado)

# Difícil: Transforme uma string bagunçada em uma lista de palavras capitalizadas, sem espaços extras.
texto = "   python,   java, c++ ,  go "
palavras = [p.strip().capitalize() for p in texto.split(",")]
print(palavras)