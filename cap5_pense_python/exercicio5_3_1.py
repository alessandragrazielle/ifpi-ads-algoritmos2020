def is_triangle(a, b, c):
    if a > b+c or b > a+c or c > a+b:
        print('No')
    else:
        print('Yes')


is_triangle(1, 12, 1)