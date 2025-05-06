# Difícil
flag_etapa1 = False
resposta = input("Você completou a etapa 1? (s/n): ")
if resposta.lower() == 's':
    flag_etapa1 = True
if flag_etapa1:
    print("Pode prosseguir para etapa 2.")
else:
    print("Você precisa completar a etapa 1 primeiro.")