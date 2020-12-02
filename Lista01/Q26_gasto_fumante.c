#include <stdio.h>

/*Calcule a quantidade de dinheiro gasta por um fumante. Dados de entrada: o número de anos que ele fuma, o
no de cigarros fumados por dia e o preço de uma carteira (1 carteira tem 20 cigarros).*/

int main() {
    int anosFumando, cigarrosDia, qtdCigarros;
    float gasto, precoCarteira;

    printf("Numero de anos fumando: ");
    scanf("%d", &anosFumando);

    printf("Numero de cigarros fumados por dia: ");
    scanf("%d", &cigarrosDia);

    printf("Preco de uma carteira de cigarros: ");
    scanf("%d", &precoCarteira);

    qtdCigarros = cigarrosDia * 365 * anosFumando;

    gasto = (qtdCigarros - (qtdCigarros%20)) / 20;

    printf("O preco total gasto foi de, aproximadamente R$%.2f", gasto);
}