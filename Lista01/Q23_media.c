#include <stdio.h>

/*Leia 3 números, calcule e escreva a média dos números.*/

int main() {
    float num1, num2, num3, media;

    printf("Digite 3 numeros: ");
    scanf("%f %f %f", &num1, &num2, &num3);

    media = (num1+num2+num3) / 3;

    printf("O valor da media dos numeros equivale a %.2f.", media);
}
