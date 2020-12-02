#include <stdio.h>

/* Leia uma velocidade em m/s, calcule e escreva esta velocidade em km/h. (Vkm/h = Vm/s * 3.6) */

int main () {
	float ms, kmh;
	
	printf("Velocidade em m/s: ");
	scanf("%f", &ms);
	
	kmh = ms*3.6;
	
	printf("%.2fm/s equivale(m) a %.2fkm/h", ms, kmh); 				
}
