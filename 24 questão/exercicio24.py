def afd_duas_vezes_010(entrada):
    estado_atual = 'q0'
    contagem_010 = 0
    
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
                contagem_010 += 1
                estado_atual = 'q1'
                if contagem_010 >= 2:
                    return True
                
    return False

# Teste
print(afd_duas_vezes_010("0101010"))  # True
print(afd_duas_vezes_010("101010"))   # False
