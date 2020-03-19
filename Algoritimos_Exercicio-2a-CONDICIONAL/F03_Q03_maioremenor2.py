num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
num3 = int(input('Número 3: '))


def numeros():
    if num1 == num2 == num3:
        print('Os números são iguais')
    elif num1 > num2 and num1 > num3:
        print(f'O {num1} é o maior')
    elif num2 > num1 and num2 > num3:
        print(f'O {num2} é o maior')
    else:
        print(f'O {num3} é o maior')
        

numeros()