def afn_a_antes_de_b(entrada):
    estado_atual = 'q0'
    
    for simbolo in entrada:
        if estado_atual == 'q0':
            if simbolo == 'a':
                estado_atual = 'q0'
            elif simbolo == 'b':
                estado_atual = 'q1'
        elif estado_atual == 'q1':
            if simbolo == 'a':
                return False
    
    return True

# Teste
print(afn_a_antes_de_b("aaabbb"))  # True
print(afn_a_antes_de_b("aababb"))  # False
print(afn_a_antes_de_b("bbb"))     # True
print(afn_a_antes_de_b("aaaa"))    # True
print(afn_a_antes_de_b("ba"))      # False
