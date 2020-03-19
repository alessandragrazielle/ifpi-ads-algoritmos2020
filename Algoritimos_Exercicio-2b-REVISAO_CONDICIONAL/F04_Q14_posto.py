combustivel = input('Tipo do combustível: ')
litros = float(input('Quantidade de litros: '))

preco_a = 1.90 * litros
preco_g = 2.50 * litros

def main():
    valor = preco_sem_desconto() - desconto()
    print(f'Valor a ser pago: R${valor}')


def preco_sem_desconto():
    if combustivel == 'A':
        return preco_a
    else:
        return preco_g


def desconto():
    if combustivel == 'A':
        if litros >= 20:
            return (1.90*3 / 100) * litros
        else:
            return (1.90*5 / 100) * litros

    else:
        if litros >= 20:
            return (2.50*4 / 100) * litros
        else:
            return (2.50*6 / 100) * litros


main()
