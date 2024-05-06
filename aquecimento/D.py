letras = [0] * 26
ans = 0
p1 = input()
p2 = input()

for char in p1:
    letras[ord(char) - ord('a')] += 1

for char in p2:
    letras[ord(char) - ord('a')] += 1

for count in letras:
    if count > ans:
        ans = count

if ans < 3:
    print("SIM")
else:
    print("NAO")
