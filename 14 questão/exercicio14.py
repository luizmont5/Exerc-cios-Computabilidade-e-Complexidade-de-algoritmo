def afn_sem_11_e_00(entrada):
    for i in range(len(entrada) - 1):
        if entrada[i:i+2] == '11' or entrada[i:i+2] == '00':
            return False
    return True

print(afn_sem_11_e_00("101010"))  # True
print(afn_sem_11_e_00("1100"))    # False
