def afd_termina_com_1(entrada):
    estado_atual = 'q0'  # estado inicial
    for simbolo in entrada:
        if estado_atual == 'q0':
            if simbolo == '0':
                estado_atual = 'q0'
            elif simbolo == '1':
                estado_atual = 'q1'
        elif estado_atual == 'q1':
            if simbolo == '0':
                estado_atual = 'q0'
            elif simbolo == '1':
                estado_atual = 'q1'
    
    
    return estado_atual == 'q1'

# Teste
print(afd_termina_com_1("101"))  # True
print(afd_termina_com_1("100"))  # False
