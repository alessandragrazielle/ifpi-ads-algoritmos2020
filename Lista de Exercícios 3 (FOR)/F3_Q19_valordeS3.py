n = int(input('Valor de N: '))
contador = 1
x = n
s = 0

for a in range(n):
    if contador % 2 == 0:
        s = s - (x/contador)
    else:
        s = s + (contador/x)

    contador += 1
    x -= 1

print(f'S = {s}')

