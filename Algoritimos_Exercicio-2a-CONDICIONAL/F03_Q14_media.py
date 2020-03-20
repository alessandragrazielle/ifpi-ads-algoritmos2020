num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
num3 = int(input('Número 3: '))
num4 = int(input('Número 4: '))
num5 = int(input('Número 5: '))


def main():
    print(f'A média é: {media()} \nE o(s) númpero(s) maior(es) que a média é(são): \n{maior1()} \n{maior2()} \n{maior3()} \n{maior4()} \n{maior5()}')

def media():
    media = (num1 + num2 + num3 + num4 + num5) / 5
    return media

def maior1():
    if num1 > media():
        return num1
    else:
        return ''

def maior2():
    if num2 > media():
        return num2 
    else:
        return ''

def maior3():
    if num3 > media():
        return num3
    else:
        return ''

def maior4():
    if num4 > media():
        return num4
    else:
        return ''

def maior5():
    if num5 > media():
        return num5
    else:
        return ''


main()