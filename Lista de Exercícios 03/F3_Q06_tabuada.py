y = 1
x = 1

while x <= 10:
    while y <= 10:
        print(f'{x} * {y} = {y*x}')

        y += 1
    
    print('         ')
    y = 1
    x += 1