# Ler a entrada como uma linha de números inteiros separados por espaço
valores_lidos = input().split()

# Converter os valores lidos para uma lista de inteiros
bits_lidos = [int(valor) for valor in valores_lidos]

# Verificar se todos os bits foram lidos com sucesso
todos_bits_lidos = all(bit != 9 for bit in bits_lidos)

# Exibir o resultado
if todos_bits_lidos:
    print("S")
else:
    print("F")