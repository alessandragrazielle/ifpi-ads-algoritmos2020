num = int(input('Digite um número de 4 dígitos: '))


def main():
    print(f'O número digitado {quadrado()} às características')


def quadrado():
    if (num//100 + num%100)**2 == num:
        return 'obedece'
    else:
        return 'não obedece'


main()
