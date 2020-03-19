num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))


def numeros():
    if num1 == num2:
        print('Os números são iguais')
    elif num1 > num2:
        print(f'O {num1} é o maior e {num2} o menor')
    else:
        print(f'O {num2} é o maior e {num1} o menor')
        

numeros()