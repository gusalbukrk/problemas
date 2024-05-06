digitos = [
    ".***..",  # 0
    "*.....",
    "*.*...",
    "**....",
    "**.*..",
    "*..*..",
    "***...",
    "****..",
    "*.**..",
    ".**..."  # 9
]

D = int(input())

entrada = [input() for _ in range(3)]

cedulas = []

for i in range(D):
    cedula = [""] * 6

    for j in range(3):
        for k in range(i * 3, i * 3 + 2):
            cedula[j * 2 + k % 3] = entrada[j][k]

    for idx, digito in enumerate(digitos):
        if digito == "".join(cedula):
            print(idx, end="")
            break

print()