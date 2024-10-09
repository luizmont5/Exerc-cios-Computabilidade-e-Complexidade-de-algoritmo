def afn_comprimento_par(entrada):
    return len(entrada) % 2 == 0

# Teste
print(afn_comprimento_par("aabb"))  # True
print(afn_comprimento_par("abc"))   # False
