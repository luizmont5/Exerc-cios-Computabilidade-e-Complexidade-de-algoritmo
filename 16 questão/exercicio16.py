def afd_blocos_consecutivos_de_zeros(entrada):
    estado_atual = 'q0'  # estado inicial
    for i in range(1, len(entrada)):
        if entrada[i] == '0' and entrada[i - 1] == '1':
            estado_atual = 'q1'
        if estado_atual == 'q1' and entrada[i] == '0':
            return False 
    
    return True

# Teste
print(afd_blocos_consecutivos_de_zeros("111000111"))  # True
print(afd_blocos_consecutivos_de_zeros("101001"))     # False
