t = (input('Em que tuno você estuda? '))


def turno():
    if t == 'M':
        print('Bom dia!')
    elif t == 'V':
        print('Boa tarde!')
    elif t == 'N':
        print('Boa noite!')
    else:
        print('Valor Inválido!')


turno()