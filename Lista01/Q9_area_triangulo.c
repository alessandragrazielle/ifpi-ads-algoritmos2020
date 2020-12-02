#include <stdio.h>

/*Leia o valor da base e altura de um triângulo, calcule e escreva sua área. (área=(base * altura)/2)*/

int main() {
    float area, base, altura;

    printf("Valor da base e altura, respectivamente: ");
    scanf("%f %f", &base, &altura);

    area = (base*altura) / 2;

    printf("Valor da area do triangulo: %.1f", area);
}