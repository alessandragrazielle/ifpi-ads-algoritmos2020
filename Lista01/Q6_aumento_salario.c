#include <stdio.h>

/*Leia o sal�rio de um trabalhador e escreva seu novo sal�rio com um aumento de 25%.*/

int main() {
    float s_atual, novo_s;

    printf("Valor do salario: R$ ");
    scanf("%f", &s_atual);

    novo_s = s_atual + (s_atual*25/100);

    printf("Valor do novo salario: R$ %.2f", novo_s);
}
