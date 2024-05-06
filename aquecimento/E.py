# Lê os pontos de conexão do primeiro conector
conector1 = input().split()

# Lê os pontos de conexão do segundo conector
conector2 = input().split()

# Função para verificar se os conectores são compatíveis
def sao_compativeis(conector1, conector2):
    for i in range(len(conector1)):
        if conector1[i] == conector2[i]:
            return False
    return True


# Verifica se os conectores são compatíveis e imprime o resultado
if sao_compativeis(conector1, conector2):
    print("S")
else:
    print("N")
