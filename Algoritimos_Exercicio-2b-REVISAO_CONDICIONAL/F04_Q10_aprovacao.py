n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

media = (n1+n2) / 2


def main():
    print(f'Notas: {n1} e {n2} \nMédia: {media} \nConceito: {conceito()} \n{aprovacao()}')


def conceito():
    if 9 < media <= 10:
        return 'A'
    elif 7.5 < media <= 9:
        return 'B'
    elif 6 < media <= 7.5:
        return 'C'
    elif 4 < media <= 6:
        return 'D'
    else:
        return 'E'


def aprovacao():
    if conceito() == 'A' or conceito() == 'B' or conceito() == 'C':
        return 'APROVADO!'
    elif conceito() == 'D' or conceito() == 'E':
        return 'REPROVADO!'


main()
    