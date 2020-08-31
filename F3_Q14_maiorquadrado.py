from math import sqrt

n = int(input('Digite um número: '))

for a in range(n):
    if sqrt(n) == int(sqrt(n)):
        print(f'O maior quadrado é {n}')
        break
    else:
        n -= 1