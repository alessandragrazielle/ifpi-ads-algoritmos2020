n = int(input('Número: '))
x = 1
y = n

while 1 <= y:
    fat = y * x
    x = fat
    y -= 1

print(f'O fatorial de {n} é {fat}')
