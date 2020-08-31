n = int(input('Número: '))
x = 1
y = n

for a in range(y):
    fat = y * x
    x = fat
    y -= 1

print(f'O fatorial de {n} é {fat}')