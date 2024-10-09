def afd_mais_uns_que_zeros(entrada):
    contador_1 = 0
    contador_0 = 0
    
    for simbolo in entrada:
        if simbolo == '1':
            contador_1 += 1
        elif simbolo == '0':
            contador_0 += 1
  
    return contador_1 > contador_0

# Teste
print(afd_mais_uns_que_zeros("11001"))  # True
print(afd_mais_uns_que_zeros("100"))    # False
