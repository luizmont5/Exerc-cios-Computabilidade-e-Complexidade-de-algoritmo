def afd_pelo_menos_um_0(entrada):
    estado_atual = 'q0'  # Estado inicial
    for simbolo in entrada:
        if simbolo == '0':
            return True  
    return False  

# Teste
print(afd_pelo_menos_um_0("1111"))  # False
print(afd_pelo_menos_um_0("1011"))  # True
