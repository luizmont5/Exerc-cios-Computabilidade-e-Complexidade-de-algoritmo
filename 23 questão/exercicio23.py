def afn_contem_101_ou_110(entrada):
    estado_101 = 'q0'
    estado_110 = 'q0'
    
    for simbolo in entrada:
        
        if estado_101 == 'q0':
            if simbolo == '1':
                estado_101 = 'q1'
        elif estado_101 == 'q1':
            if simbolo == '0':
                estado_101 = 'q2'
            elif simbolo == '1':
                estado_101 = 'q1'
        elif estado_101 == 'q2':
            if simbolo == '1':
                return True 

        if estado_110 == 'q0':
            if simbolo == '1':
                estado_110 = 'q1'
        elif estado_110 == 'q1':
            if simbolo == '1':
                estado_110 = 'q2'
            elif simbolo == '0':
                estado_110 = 'q1'
        elif estado_110 == 'q2':
            if simbolo == '0':
                return True 
    return False 

# Teste
print(afn_contem_101_ou_110("1010"))  # True
print(afn_contem_101_ou_110("1001"))  # False
