a = int(input('Coeficiente A: '))
b = int(input('Coeficiente B: '))
c = int(input('Coeficiente C: '))


def valores_x():
    if a != 0:
        delta = b**2 - 4*a*c
        x1 = (-b + delta**0.5) / 2*a
        x2 = (-b - delta**0.5) / 2*a

        raizA1 = a * x1**2
        raizA2 = a * x2**2
        raizB1 = b * x1
        raizB2 = b * x2

        print(f'Raízes de A: {raizA1} e {raizA2} \nRaízes de B: {raizB1} e {raizB2} \nRaíz de C: {c}')

    else:
        print('Essa não é uma equação do segundo grau')
    

valores_x()