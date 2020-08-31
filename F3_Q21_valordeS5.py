x = 1
y = 1
z = 0

while x <= 99 and y <= 50:
    s = (x/y) + z
    z = s

    x += 2
    y += 1

print(f'S = {s}')