morangos = float(input('Quantidade em kg de morangos adquiridos: '))
macas = float(input('Quantidade em kg de maçãs adquiridas: '))


def main():
    valor_total = preco_morango() + preco_maca()
    valor_final = valor_total - desconto()
    print(f'Valor a ser pago: R${valor_final}')


def desconto():
    valor_total = preco_morango() + preco_maca()
    if morangos + macas > 8 or valor_total > 25:
        return valor_total * 10/100
    else: 
        return 0


def preco_morango():
    if morangos <= 5:
        return 2.50 * morangos
    else:
        return 2.20 * morangos


def preco_maca():
    if macas <= 5:
        return 1.80 * macas
    else:
        return 1.50 * macas


main()