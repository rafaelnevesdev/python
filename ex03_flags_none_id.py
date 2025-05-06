# Desafio 3: Flags, None, is, is not, id

# Fácil: Crie uma variável como None e use is para verificar antes de continuar.
x = None
if x is None:
    print("x ainda não foi inicializado.")

# Médio: Use duas variáveis iguais e compare com id() antes e depois de alterar uma.
a = [1, 2, 3]
b = a
print("Antes:", id(a), id(b))
b = [1, 2, 3]
print("Depois:", id(a), id(b))

# Difícil: Implementação de flag de controle para saber se o usuário passou por uma etapa.
flag_etapa = False
resposta = input("Digite 'ok' para passar para a próxima etapa: ")
if resposta.lower() == "ok":
    flag_etapa = True

if flag_etapa:
    print("Usuário passou pela etapa!")
else:
    print("Usuário NÃO passou pela etapa.")