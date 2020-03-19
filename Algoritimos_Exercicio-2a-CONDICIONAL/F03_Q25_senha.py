s = int(input('Digite a senha: '))


def validade():
    if s == 1234:
        print('PERMISSÃO CONCEDIDA!')
    else:
        print('PERMISSÃO NEGADA!')


validade()
