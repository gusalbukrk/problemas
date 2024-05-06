# Passo 1: Ler entrada
N, C, S = map(int, input().split())


# Passo 2: Ler sequência de comandos
comandos = list(map(int, input().split()))

# Passo 3: Inicializar variáveis
estacao_atual = 1
contador_estacao_S = 0

# Passo 4 e 5: Iterar pelos comandos
for comando in comandos:
    if estacao_atual == S:
        contador_estacao_S += 1
    
    # Atualizar a estação atual de acordo com o comando
    estacao_atual += comando
    
    # Garantir que a estação atual esteja dentro dos limites (1 a N)
    if estacao_atual > N:
        estacao_atual = 1
    elif estacao_atual < 1:
        estacao_atual = N

# Passo 6: Verificar a última estação após o loop
if estacao_atual == S:
    contador_estacao_S += 1

# Passo 7: Imprimir a saída
print(contador_estacao_S)
