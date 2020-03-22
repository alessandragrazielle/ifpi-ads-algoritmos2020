h1 = int(input('Hora em que o jogo começa: '))
m1 = int(input('Minuto em que o jogo começa: '))
h2 = int(input('Hora em que o jogo acaba: '))
m2 = int(input('Minuto em que o jogo acaba: '))


def main():
    print(f'A duração do jogo é de {horas()}h e {minutos()}min')


def horas():
    if h1 < h2:
        if m1 > m2:
            return h2 - h1 - 1
        else:
            return h2 - h1

    elif h1 > h2:
        return 24 - h1 + h2

    else:
        if m1 > m2:
            return 23
        elif m1 < m2:
            return 0
        else:
            return 24


def minutos():
    if m1 > m2:
        return 60 - m1
    elif m2 > m1:
        return m2 - m1
    else:
        return 0


main()
