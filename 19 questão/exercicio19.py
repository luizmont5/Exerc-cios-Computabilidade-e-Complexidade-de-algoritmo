def afn_contem_010(entrada):
    estado_atual = 'q0'
    
    for simbolo in entrada:
        if estado_atual == 'q0':
            if simbolo == '0':
                estado_atual = 'q1'
        elif estado_atual == 'q1':
            if simbolo == '1':
                estado_atual = 'q2'
            elif simbolo == '0':
                estado_atual = 'q1'
        elif estado_atual == 'q2':
            if simbolo == '0':
                return True
    
    return False

# Teste
print(afn_contem_010("1010"))  # True
print(afn_contem_010("1101"))  # False
