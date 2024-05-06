N = int(input())
entrada = input()

contador = 0

for i, letter in enumerate(entrada):
    if ( letter == 'a' and ( (i != 0 and entrada[i - 1] == 'a') or (i != len(entrada) - 1) and entrada[i + 1] == 'a') ):
        contador += 1

print(contador)

