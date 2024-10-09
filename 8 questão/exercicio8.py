def afn_zeros_divisivel_por_3(entrada):
    contador_0 = 0
    
    for simbolo in entrada:
        if simbolo == '0':
            contador_0 += 1
    
    return contador_0 % 3 == 0

# Teste
print(afn_zeros_divisivel_por_3("000111"))  # True
print(afn_zeros_divisivel_por_3("00101"))   # False
