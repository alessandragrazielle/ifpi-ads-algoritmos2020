n = int(input('Valor de N: '))
contador = 1
s = 0

for a in range(n):
    if contador%2 == 0: 
        s = s - (1/contador)
    else:
        s = s + (1/contador)

    contador += 1

print(f'S = {s}')
