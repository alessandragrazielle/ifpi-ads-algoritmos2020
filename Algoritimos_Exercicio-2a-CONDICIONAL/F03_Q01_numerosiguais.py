num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
num3 = int(input('Número 3: '))


def main():
    n = numeros()
    print(f'Existem {n} númperos iguais')

def numeros():
    if num1 == num2 == num3:
        return 3
    elif num1 == num2 or num2 == num3 or num1 == num3:
        return 2
    else:
        return 0


main()