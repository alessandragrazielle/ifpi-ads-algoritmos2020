#include <stdio.h>

/*Leia um número inteiro de horas, calcule e escreva quantas semanas, quantos dias e quantas horas ele
corresponde.*/

int main() {
    int h, semanas, dias, horas;

    printf("Quantidade de horas: ");
    scanf("%d", &h);

    semanas = (h - (h%168)) / 168; // uma semana tem 168 horas
    horas = (h % 168) % 24;
    dias = (h - semanas*168 - horas) / 24;

    printf("%d semana(s), %d dia(s) e %d hora(s)", semanas, dias, horas);
}
