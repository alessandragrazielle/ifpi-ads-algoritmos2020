num = float(input('Digite um número: '))


def main():
    print(f'O número arredondado é: {arredondar()}')


def arredondar():
    if (num - num//1) < 0.5:
        return num - (num - num//1)
    else:
        return num + 1 - (num - num//1)


main()