T, D, M = map(int, input().split())
tempos_refeicoes = sorted([int(input()) for _ in range(M)])

pode_descansar = False

if M == 0:
    if D >= T:
        pode_descansar = True
else:
    intervalo_anterior = 0
    for tempo_refeicao in tempos_refeicoes:
        intervalo_entre_refeicoes = tempo_refeicao - intervalo_anterior
        if intervalo_entre_refeicoes >= T:
            pode_descansar = True
        intervalo_anterior = tempo_refeicao

    intervalo_final = D - tempos_refeicoes[-1]
    if intervalo_final >= T:
        pode_descansar = True

if pode_descansar:
    print('S')
else:
    print('N')
