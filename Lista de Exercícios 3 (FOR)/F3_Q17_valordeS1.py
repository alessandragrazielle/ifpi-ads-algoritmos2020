n = int(input('Número: '))
x = 1
y = 0

for a in range(n):
    s = y + (1/x)
    y = s

    x += 1

print(f'S = {s}')