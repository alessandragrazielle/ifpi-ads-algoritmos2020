n = int(input('Número: '))
x = 1
y = 0
z = n

while x <= z:
    s = y + (x/n)
    y = s

    x += 1
    n -= 1

print(f'S = {s}')