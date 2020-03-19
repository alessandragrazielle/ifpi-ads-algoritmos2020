num = int(input('Digite um número de 1 à 100: '))


def numero():
    if num == 2 or num == 3 or num == 5 or num == 7:
        print('O número é primo')
    else:
        if num%2 == 0 or num%3 == 0 or num%5 == 0 or num%7 == 0:
            print(f'O número não é primo')
        else:
            print(f'O número é primo')
        

        

numero()