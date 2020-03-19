num = float(input('Digite um número: '))


def main():
    print (f'O número {num} é {tipo()}')


def tipo():
    if num % 1 == 0:
        return 'inteiro'
    else:
        return 'decimal'



main()