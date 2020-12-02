#include <stdio.h>

/*Leia uma temperatura em °F, calcule e escreva a equivalente em °C. (t°C = (5 * t°F - 160) / 9).*/

int main() {
    float tf, tc;
    
    printf("Temperatura em : ");
    scanf("%f", &tf);

    tc = (5 * tf - 160) / 9;

    printf("%.1f graus Fahrenheit equivale a %.1f graus Celsius", tf, tc);
}
