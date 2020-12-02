#include <stdio.h>

/*Sabendo que latão é constituído de 70% de cobre e 30% de zinco, escreva um programa que calcule a
quantidade de cada um desses componentes para se obter certa quantidade de latão (em kg), informada pelo
usuário.*/

int main() {
    float qtdLatao, zinco, cobre;

    printf("Quantidade de latao epm kg: ");
    scanf("%f", &qtdLatao);

    cobre = qtdLatao * 70/100;
    zinco = qtdLatao - cobre;

    printf("Em %.2fkg de latao, tem %.2fkg de cobre e %.2fkg de zinco", qtdLatao, cobre, zinco);
}