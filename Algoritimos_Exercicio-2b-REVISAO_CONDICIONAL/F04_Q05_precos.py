pre1 = float(input('Preço 1: '))
pre2 = float(input('Preço 2: '))
pre3 = float(input('Preço 3: '))


def main():
    print(f'O produto que deve ser comprado é: {produto()}')

def produto():
    if pre1 == pre2 == pre3:
        return 'Qualquer um'
    elif pre1 < pre2 and pre1 < pre3:
        return 'O produto 1'
    elif pre2 < pre1 and pre2 < pre3:
        return 'O produto 2'
    else:
        return 'O produto 3'


main()