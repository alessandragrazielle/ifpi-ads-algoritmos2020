print('DIGITE O VALOR DE 3 LADOS DE UM TRIÂNGULO (A SOMA DE 2 LADOS NÃO PODE SER MENOR QUE O TERCEIRO)')
lado1 = int(input('Lado 1: '))
lado2 = int(input('Lado 2: '))
lado3 = int(input('Lado 3: '))


def main():
    l = lados()
    print(f'O triângulo é {l}')


def lados():
    if lado1 == lado2 == lado3:
        return 'equilátero'
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return 'isósceles'
    else:
        return 'escaleno'


main()