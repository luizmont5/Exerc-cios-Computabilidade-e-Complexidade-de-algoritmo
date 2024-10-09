def afd_exatamente_um_ab(entrada):
    estado_atual = 'q0'
    ab_encontrado = False
    
    for simbolo in entrada:
        if estado_atual == 'q0':
            if simbolo == 'a':
                estado_atual = 'q1'
        elif estado_atual == 'q1':
            if simbolo == 'b':
                if ab_encontrado:
                    return False
                ab_encontrado = True
                estado_atual = 'q0'
            elif simbolo == 'a':
                estado_atual = 'q1'
  
    return ab_encontrado

# Teste
print(afd_exatamente_um_ab("aab"))  # True
print(afd_exatamente_um_ab("abab")) # False
