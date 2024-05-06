#include <stdio.h>

int main(void) {
    int C, A;
    scanf("%d %d", &C, &A);
    int quociente = A / (C - 1);
    int resto = A % (C - 1);
    int resposta = quociente;
    if (resto > 0) resposta++;
    printf("%d\n", resposta);
    return 0;
}
