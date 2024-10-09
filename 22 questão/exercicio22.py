def afd_diferenca_multiplos_de_3(entrada):
    estado_atual = 0
    
    for simbolo in entrada:
        if simbolo == 'a':
            estado_atual = (estado_atual + 1) % 3
        elif simbolo == 'b':
            estado_atual = (estado_atual - 1) % 3
    
    return estado_atual == 0

# Teste
print(afd_diferenca_multiplos_de_3("aaabbb"))  # True
print(afd_diferenca_multiplos_de_3("aab"))     # False
