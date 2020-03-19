num = int(input('Digite um número de 4 dígitos: '))


def quadrado():
    if num**0.5 == (num//100 + num%100):
        print(f'O número {num} é um quadrado perfeito')
    else:
        print(f'O número {num} não é um quadrado perfeito')


quadrado()
