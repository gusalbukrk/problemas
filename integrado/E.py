def e_um_pangrama(s):
    # Define um conjunto vazio para armazenar as letras únicas na sequência
    letras = set()

    # Converte a sequência para letras minúsculas para garantir a contagem correta
    s = s.lower()

    # Percorre cada caractere na sequência
    for char in s:
        # Verifica se o caractere é uma letra minúscula
        if 'a' <= char <= 'z':
            # Adiciona o caractere ao conjunto de letras
            letras.add(char)

    # Verifica se o conjunto de letras contém todas as 26 letras do alfabeto
    return len(letras) == 26

# Lê a sequência da entrada padrão
sequencia = input()

# Verifica se a sequência é um pangrama e imprime 'S' ou 'N'
if e_um_pangrama(sequencia):
    print('S')
else:
    print('N')
