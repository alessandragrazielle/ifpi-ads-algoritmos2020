num1 = float(input('Número 1: '))
num2 = float(input('Número 2: '))
ope = float(input('Número da operação a ser realizada: '))


def main():
    print(f'O resultado é: {calculo()}')


def calculo():
    if ope == 1:
        return num1 + num2
    elif ope == 2:
        return num1 - num2
    elif ope == 3:
        return num1 * num2
    elif ope == 4:
        return num1 / num2
    else:
        return 'Operação Inválida!'


main()

