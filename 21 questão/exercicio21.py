def afn_a_apos_cada_b(entrada):
    encontrou_b = False
    
    for simbolo in entrada:
        if simbolo == 'b':
            encontrou_b = True
        elif simbolo == 'a' and encontrou_b:
            encontrou_b = False
  
    return not encontrou_b

# Teste
print(afn_a_apos_cada_b("aabb"))   # True
print(afn_a_apos_cada_b("abab"))   # False
