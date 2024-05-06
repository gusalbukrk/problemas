def contar_posicoes_possiveis(mensagem, crib):
    count = 0
    mensagem_len = len(mensagem)
    crib_len = len(crib)
    
    for i in range(mensagem_len - crib_len + 1):
        match = True
        for j in range(crib_len):
            if mensagem[i + j] == crib[j]:
                match = False
                break
        if match:
            count += 1
    
    return count

mensagem = input()
crib = input()

resultado = contar_posicoes_possiveis(mensagem, crib)
    
print(resultado)
