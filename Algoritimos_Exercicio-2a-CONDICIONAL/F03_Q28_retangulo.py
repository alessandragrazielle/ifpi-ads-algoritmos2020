x = int(input('Coordenada x: '))
y = int(input('Coordenada y: '))


def main():
    area = xs() * ys()
    print(f'A área do retângulo é {area}')


def xs():
    if x < 0:
         return x*-1
    else:
        return x


def ys():
    if y < 0:
         return y*-1
    else:
        return y


main()
