#include <stdio.h>

/*Leia o valor do lado de um quadrado, calcule e escreva sua área. (área = lado2)*/

int main() {
    float area, lado;

    printf("Valor do lado do quadrado: ");
    scanf("%f", &lado);

    area = lado*lado;

    printf("Valor da area do quadrado: %.1f", area);
}