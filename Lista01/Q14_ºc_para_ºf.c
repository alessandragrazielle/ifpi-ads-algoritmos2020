#include <stdio.h>

/*Leia uma temperatura em °C, calcule e escreva a equivalente em °F. (t°F = (9 * t°C + 160) / 5)*/

int main() {
    float tc, tf;
    
    printf("Temperatura em : ");
    scanf("%f", &tc);

    tf = (9 * tc + 160) / 5;

    printf("%.1f graus Celsius equivale a %.1f graus Fahrenheit", tc, tf);
}
