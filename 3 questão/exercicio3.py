def afd_exatamente_dois_1s(entrada):
    estado_atual = 'q0'  # Estado inicial
    for simbolo in entrada:
        if estado_atual == 'q0':
            if simbolo == '1':
                estado_atual = 'q1'
        elif estado_atual == 'q1':
            if simbolo == '1':
                estado_atual = 'q2'
            elif simbolo == '0':
                estado_atual = 'q1'
        elif estado_atual == 'q2':
            if simbolo == '1':
                return False  
            elif simbolo == '0':
                estado_atual = 'q2'

    return estado_atual == 'q2'

# Teste
print(afd_exatamente_dois_1s("00100"))  # False
print(afd_exatamente_dois_1s("00101"))  # True
