print ('DIGITE 3 NÚMEROS DIFERENTES')
num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
num3 = int(input('Número 3: '))


def ordem():
    if num1 > num2 > num3:
        print(f'{num1}>{num2}>{num3}')
    elif num1 > num3 > num2:
        print(f'{num1}>{num3}>{num2}')
    elif num2 > num1 > num3:
        print(f'{num2}>{num1}>{num3}')
    elif num2 > num3 > num1:
        print(f'{num2}>{num3}>{num1}')
    elif num3 > num1 > num2:
        print(f'{num3}>{num1}>{num2}')
    elif num3 > num2 > num1:
        print(f'{num3}>{num2}>{num1}')


ordem()