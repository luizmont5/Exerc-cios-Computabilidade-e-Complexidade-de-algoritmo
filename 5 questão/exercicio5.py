def afd_comeca_e_termina_mesmo(entrada):
    if len(entrada) == 0:
        return False  
    
    return entrada[0] == entrada[-1]  

# Teste
print(afd_comeca_e_termina_mesmo("101"))  # True
print(afd_comeca_e_termina_mesmo("100"))  # False
