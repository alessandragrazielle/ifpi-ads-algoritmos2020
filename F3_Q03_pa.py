a = int(input('Valor inicial: '))
l = int(input('Limite: '))
r = int(input('Razão: '))

for i in range(a, l, r):
    print(a, end=' ')
    a += r