# Fácil
try:
    texto = "Python"
    texto[0] = "J"  # Isso dará erro
except TypeError as e:
    print(f"Erro: {e}")