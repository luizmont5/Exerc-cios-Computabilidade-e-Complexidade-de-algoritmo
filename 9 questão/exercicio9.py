def afd_contem_101(entrada):
    estado_atual = 'q0'  # estado inicial
    for simbolo in entrada:
        if estado_atual == 'q0':
            if simbolo == '1':
                estado_atual = 'q1'
        elif estado_atual == 'q1':
            if simbolo == '0':
                estado_atual = 'q2'
            elif simbolo == '1':
                estado_atual = 'q1'
        elif estado_atual == 'q2':
            if simbolo == '1':
                estado_atual = 'q3'
            else:
                estado_atual = 'q0'
    
    return estado_atual == 'q3'

# Teste
print(afd_contem_101("110101"))  # True
print(afd_contem_101("10001"))  # False
