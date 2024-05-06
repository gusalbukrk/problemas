from functools import reduce

def cartaParaValor(l):
  return list(map(lambda n: n if n <= 10 else 10, l))

def sum(l):
  return reduce(lambda acc, cur: acc + cur, cartaParaValor(l))

N = int(input())
joao = [int(n) for n in input().split()]
maria = [int(n) for n in input().split()]
comuns = [int(n) for n in input().split()]

if (N == 8):
  if (
    sum(maria + comuns) <
    sum(joao + comuns)
  ):
    print(-1)

  exit()

# joao precisa de no mínimo esse valor para estourar
minJoao = 24 - sum(joao + comuns)

# maria precisa de exatamente esse valor para ganhar
minMaria = 23 - sum(maria + comuns)

# retiradas = joao + maria + comuns  # todas cartas já retiradas
retiradas = cartaParaValor(joao + maria + comuns)  # todos valores já retirados

if (retiradas.count(minMaria) == 4 if minMaria < 10 else retiradas.count(minMaria) == 16):
  print(-1)
  exit()

while ( # para (ou não começa) quando minJoao > 10 porque não há carta com valor maior que 10
  retiradas.count(minJoao) == 4 if minJoao != 10 else retiradas.count(minJoao) == 16
):
  minJoao += 1

p = []

if (minMaria <= 10):
  p.append(minMaria)

if (minJoao <= 10):
  p.append(minJoao)

if len(p) == 0:
  print(-1)
else:
  print(min(p))
