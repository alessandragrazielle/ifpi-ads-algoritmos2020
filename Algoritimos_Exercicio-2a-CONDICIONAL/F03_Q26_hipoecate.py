lado1 = int(input('Lado 1: '))
lado2 = int(input('Lado 2: '))
lado3 = int(input('Lado 3: '))


def main():
    print(f'A hipotenusa é o {lados()} e os outros lados são os catetos')


def lados():
    if lado1 > lado2 > lado3 or lado1 > lado3 > lado2:
        return 'lado 1'
    elif lado2 > lado1 > lado3 or lado2 > lado3 > lado1:
        return 'lado 2'
    else:
        return 'lado 3'


main()