def afd_impar_zeros_e_uns(entrada):
    estado_atual = ('q0', 'q0')
    
    for simbolo in entrada:
        if simbolo == '0':
            estado_atual = (estado_atual[0] == 'q0' and 'q1' or 'q0', estado_atual[1])
        elif simbolo == '1':
            estado_atual = (estado_atual[0], estado_atual[1] == 'q0' and 'q1' or 'q0')
    
    return estado_atual == ('q1', 'q1')

# Teste
print(afd_impar_zeros_e_uns("1010"))  # True
print(afd_impar_zeros_e_uns("1100"))  # False
