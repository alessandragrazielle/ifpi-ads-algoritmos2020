num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
num3 = int(input('Número 3: '))
num4 = int(input('Número 4: '))
num5 = int(input('Número 5: '))


def main():
    print (f'O maior número é {maior()} e o menor é {menor()}')


def maior():
    if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
        return num1
    elif num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5:
        return num2
    elif num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5:
        return num3
    elif num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5:
        return num4
    else:
        return num5


def menor():
    if num1 < num2 and num1 < num3 and num1 < num4 and num1 < num5:
        return num1
    elif num2 < num1 and num2 < num3 and num2 < num4 and num2 < num5:
        return num2
    elif num3 < num1 and num3 < num2 and num3 < num4 and num3 < num5:
        return num3
    elif num4 < num1 and num4 < num2 and num4 < num3 and num4 < num5:
        return num4
    else:
        return num5
        

main()