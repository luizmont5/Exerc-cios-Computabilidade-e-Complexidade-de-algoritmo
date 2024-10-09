def afd_numero_par_de_0s(entrada):
    estado_atual = 'q0'  # estado inicial
    for simbolo in entrada:
        if estado_atual == 'q0':
            if simbolo == '0':
                estado_atual = 'q1'
            elif simbolo == '1':
                estado_atual = 'q0'
        elif estado_atual == 'q1':
            if simbolo == '0':
                estado_atual = 'q0'
            elif simbolo == '1':
                estado_atual = 'q1'
    
    
    return estado_atual == 'q0'

# Teste
print(afd_numero_par_de_0s("1100"))  # True
print(afd_numero_par_de_0s("1010"))  # False
