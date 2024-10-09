def afn_pelo_menos_um_0(entrada):
    for simbolo in entrada:
        if simbolo == '0':
            return True  
    return False  

# Teste
print(afn_pelo_menos_um_0("1111"))  # False
print(afn_pelo_menos_um_0("1011"))  # True
