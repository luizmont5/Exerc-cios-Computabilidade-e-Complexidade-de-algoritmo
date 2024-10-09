def afn_0_seguido_de_1(entrada):
    encontrou_0 = False
    
    for simbolo in entrada:
        if simbolo == '0':
            encontrou_0 = True
        elif simbolo == '1' and encontrou_0:
            return True
    
    return False

# Teste
print(afn_0_seguido_de_1("10011"))  # True
print(afn_0_seguido_de_1("11100"))  # False
