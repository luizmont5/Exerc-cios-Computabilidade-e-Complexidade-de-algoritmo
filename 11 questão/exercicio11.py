def afd_numero_impar_de_as(entrada):
    estado_atual = 'q0' 
    for simbolo in entrada:
        if simbolo == 'a':
            estado_atual = 'q1' if estado_atual == 'q0' else 'q0' 
        
    return estado_atual == 'q1'

# Teste
print(afd_numero_impar_de_as("ababa"))  # True
print(afd_numero_impar_de_as("aabb"))   # False
