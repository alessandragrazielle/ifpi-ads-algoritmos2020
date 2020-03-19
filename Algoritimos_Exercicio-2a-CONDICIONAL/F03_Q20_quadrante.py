ang = int(input('Digite um ângulo entre 0 e 360 graus: '))

def main():
    print(f'O ângulo está no {quad()} quadrante')


def quad():
    if 0 < ang < 90:
        return 'primeiro'
    elif 90 < ang < 180:
        return 'segundo'
    elif 180 < ang < 270:
        return 'terceiro'
    else:
        return 'quarto'


main()