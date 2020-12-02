#include <stdio.h>

/*O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do distribuidor e
dos impostos (aplicados ao custo de fábrica). Supondo que a percentagem do distribuidor seja de 28% e os
impostos de 45%, escreva um programa que leia o custo de fábrica de um carro e escreva o custo ao
consumidor.*/

int main() {
    float custoFabrica, percentagemDistribuidor, impostos, custoConsumidor;

    printf("Custo de fabrica do carro: ");
    scanf("%f", &custoFabrica); // o custo de fabrica é de 27%

    custoConsumidor = (custoFabrica*100) / 27;

    printf("O custo ao consumidor sera de R$%.2f", custoConsumidor);
}
