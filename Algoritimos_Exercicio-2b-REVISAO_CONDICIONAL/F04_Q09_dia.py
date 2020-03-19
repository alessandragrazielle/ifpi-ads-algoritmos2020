n = int(input('Digite um número: '))


def main():
    print(f'O número {n} corresponde à: {dia()}')


def dia():
    if n == 1:
        return 'domingo'
    elif n == 2:
        return 'segunda'
    elif n == 3:
        return 'terça'
    elif n == 4:
        return 'quarta'
    elif n == 5:
        return 'quinta'
    elif n == 6:
        return 'sexta'
    elif n == 7:
        return 'sábado'
    else:
        return 'Valor Inválido!'


main()