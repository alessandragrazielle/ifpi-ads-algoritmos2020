#include <stdio.h>

/* Leia o valor do d�lar e um valor em d�lar, calcule e escreva o equivalente em real (R$).*/

int main() {
    float vDolar, qtdDolares, qtdReal;

    printf("Preco do dolar: ");
    scanf("%f", &vDolar);

    printf("Quantidade de dolares: ");
    scanf("%f", &qtdDolares);

    qtdReal = vDolar*qtdDolares;

    printf("$%.2f equivale(m) a R$%.2f", qtdDolares, qtdReal);
    
}

