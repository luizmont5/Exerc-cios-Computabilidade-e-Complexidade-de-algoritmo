def afn_para_afd_termina_com_01(entrada):
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
            estado_atual = 'q0' if simbolo == '0' else 'q1'
    
    return estado_atual == 'q2'

# Teste
print(afn_para_afd_termina_com_01("101"))  # True
print(afn_para_afd_termina_com_01("100"))  # False
