#include <stdio.h>

/*Leia a idade de uma pessoa expressa em dias e escreva-a expressa em anos, meses e dias.*/

int main() {
    int idadeDias, anos, meses, dias;

    printf("Sua idade em dias: ");
    scanf("%d", &idadeDias);

    anos = (idadeDias - (idadeDias%365)) / 365; 
    dias = (idadeDias % 365) % 30;
    meses = (idadeDias - anos*365 - dias) / 30;

    printf("Sua idade corresponde a %d ano(s), %d mes(es) e %d dia(s)",anos, meses, dias);
}
