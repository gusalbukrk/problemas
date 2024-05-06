# Lê a nota de uma das provas e a média entre as duas notas
A = int(input())
M = int(input())

# Calcula a nota da outra prova usando a fórmula da média
# M = (A + B) / 2, onde B é a nota da outra prova
# Multiplicamos a média por 2 para isolar B e depois subtrai A
B = (M * 2) - A

# Imprime a nota da outra prova
print(B)