#include <stdio.h>

/*Leia um valor em kg (quilograma), calcule e escreva o equivalente em g(grama).*/

int main() {
    float kg, g;

    printf("Valor em kg: ");
    scanf("%f", &kg);

    g = kg*1000;

    printf("%.1fkg equivale(m) a %.1fg", kg, g);
}
