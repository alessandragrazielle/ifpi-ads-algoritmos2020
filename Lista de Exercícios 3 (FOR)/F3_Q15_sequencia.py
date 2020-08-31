n = int(input('Quantidade de termos: '))
x = 1
y = 2

for a in range(n):
    print(x, end=' ')
    x += y
    y += 1