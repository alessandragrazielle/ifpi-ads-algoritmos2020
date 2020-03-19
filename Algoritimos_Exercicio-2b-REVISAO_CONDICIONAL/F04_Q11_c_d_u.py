num = int(input('Digite um número maior que 0 e menor que 1000: '))

u = num // 1 % 10 
d = num // 10 % 10
c = num // 100 % 10


def main():
    print(f'O número tem: {particao()}')


def particao():
    if num // 10 >= 10:
        return f'{c} {singular_cen()}, {d} {singular_dez()} e {u} {singular_uni()}'
    elif num // 10 >= 1:
        return f'{d} {singular_dez()} e {u} {singular_uni()}'
    else:
        return f'{u} {singular_uni()}'


def singular_uni():
    if u == 1:
        return 'unidade'
    else:
        return 'unidades'


def singular_dez():
    if d == 1:
        return 'dezena'
    else:
        return 'dezenas'


def singular_cen():
    if c == 1:
        return 'centena'
    else:
        return 'centenas'



main()