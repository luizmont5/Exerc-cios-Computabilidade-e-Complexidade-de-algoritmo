def afn_comeca_01_termina_10(entrada):
    if len(entrada) < 4:
        return False
    
    return entrada.startswith('01') and entrada.endswith('10')

# Teste
print(afn_comeca_01_termina_10("0110"))  # True
print(afn_comeca_01_termina_10("00110")) # False
