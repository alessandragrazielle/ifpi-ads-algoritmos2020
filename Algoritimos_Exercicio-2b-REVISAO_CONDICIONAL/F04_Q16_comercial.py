tipo = input('Tipo de carne que deseja comprar (file, alcatra ou picanha): ')
kg = float(input('Quantidade de kilos: '))
pagamento = input('Tipo de pagamento (cartão Tabajara, crédito, débito ou espécie): ')


def main():
    valor_total = carne() * kg 
    desconto = valor_total * cartao()/100
    valor_final = valor_total - desconto

    print(f'Tipo da carne: {tipo} \nQuantidade de carne: {kg}kg \nPreço total: R${valor_total} ', end='')
    print(f'\nTipo de pagamento: {pagamento} \nValor do desconto: {cartao()}% \nValor a pagar: R${valor_final}')


def carne():
    if tipo == 'file':
        if kg <= 5:
            return 4.90
        else: 
            return 5.80

    elif tipo == 'alcatra':
        if kg <= 5:
            return 5.90
        else: 
            return 6.80

    else:
        if kg <= 5:
            return 6.90
        else: 
            return 7.80


def cartao():
    if pagamento == 'cartão Tabajara':
        return 5
    else:
        return 0


main()