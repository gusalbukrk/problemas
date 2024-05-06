def maiorfat_menor_que(n):
    # O(n)
    # Encontra o maior valor p para o qual p! <= n
    product = 1
    # p: contar quantas vezes chamamos a função
    p = 1
    while product * p <= n:
        product *= p
        p += 1
    # product > n / (p+1)
    return product

def solucao(N):
    k = 0  # Contagem
    while N > 0:
        N -= maiorfat_menor_que(N)
        k += 1
    return k

if __name__ == "__main__":
    # 1 <= N <= 100,000
    N = int(input())
    k = solucao(N)
    print(k)

