peso = float(input('Seu peso (em Kg): '))
altura = float(input('Sua altura (em metros): '))


def main():
    print(f'Seu estado atual é: {imc()}')


def imc():
    imc = peso / altura**2
    if imc < 25:
        return 'peso normal'
    elif 25 < imc < 30:
        return 'obeso'
    else:
        return 'obesidade mórbida'


main()