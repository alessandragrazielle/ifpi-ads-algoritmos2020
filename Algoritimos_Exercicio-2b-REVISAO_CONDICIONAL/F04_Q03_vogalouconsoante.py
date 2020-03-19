let = (input('Digite uma letra: '))


def main():
    print(f'A letra {let} é uma {letra()}')


def letra():
    if let=='a' or let=='e' or let=='i' or let=='o' or let=='u':
        return 'vogal'
    else:
        return 'consoante'


main()