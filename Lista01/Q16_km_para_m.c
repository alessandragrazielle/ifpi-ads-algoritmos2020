#include <stdio.h>

/*Leia um valor em km, calcule e escreva o equivalente em m.*/

int main() {
    float km, m;

    printf("Valor em km: ");
    scanf("%f", &km);

    m = km*1000;

    printf("%.1fkm equivale(m) a %.1fm", km, m);
}
