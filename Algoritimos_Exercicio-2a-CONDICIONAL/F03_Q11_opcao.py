op = int(input('Valor da opção (de 1 à 3): '))
n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
n3 = int(input('Número 3: '))


def main():
    print(f'Novos números: {opcoes()}')


def opcoes():
    if op == 1:
        return n1*10, n2, n3
    elif op == 2:
        return n1, n2*10, n3
    else:
        return n1, n2, n3*10


main()