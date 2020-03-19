num = int(input('Digite um número de dois dígitos: '))


def algarismos():
    if num//10 == num%10:
        print('Os algarismos são iguais')
    else:
        print(f'Os algarismos são diferentes')
        

algarismos()