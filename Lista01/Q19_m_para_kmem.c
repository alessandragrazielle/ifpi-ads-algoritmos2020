#include <stdio.h>

/*Leia um número inteiro de metros, calcule e escreva quantos Km e quantos metros ele corresponde.*/

int main() {
    int m, valorKm, valorM;

    printf("Valor em m: ");
    scanf("%d", &m);

    valorM = m%1000;
    valorKm = (m - valorM) / 1000;

    printf("%dm equivale(m) a %dkm e %dm", m, valorKm, valorM);
}
