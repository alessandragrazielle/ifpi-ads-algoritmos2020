print('DIGITE O VALOR DE 3 ÂNGULOS DE UM TRIÂNGULO (A SOMA DE TODOS DEVE DAR 180)')
ang1 = int(input('Ângulo 1: '))
ang2 = int(input('Ângulo 2: '))
ang3 = int(input('Ângulo 3: '))


def main():
    a = angulos()
    print(f'O triângulo é {a}')


def angulos():
    if ang1 < 90 and ang2 < 90 and ang3 < 90:
        return 'acutângulo'
    elif ang1 == 90 or ang2 == 90 or ang3 == 90:
        return 'retângulo'
    elif ang1 > 90 or ang2 > 90 or ang3 > 90:
        return 'obtusângulo'


main()