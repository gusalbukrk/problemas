N = int(input())
saldo = input()[1:].split('.')[1]

x = 0

for _ in range(N):
    deposito = input()[1:].split('.')[1]

    t = int(saldo) + int(deposito)
    if (t != 100 and t != 0):
        x += 1
    saldo = str(t - 100 if t >= 100 else t)

print(x)
