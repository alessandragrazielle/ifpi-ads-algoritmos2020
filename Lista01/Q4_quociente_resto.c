#include <stdio.h>

/*Leia 2 n�meros inteiros, calcule e escreva o quociente e o resto da divis�o do 1o pelo 2o.*/

int main() {
    int x, y, quo, res;

    printf("Digite dois numeros inteiros: ");
    scanf("%d %d", &x, &y);

    quo = y/x;
    res = y%x;

    printf("Quociente: %d \nResto: %d", quo, res);
}
