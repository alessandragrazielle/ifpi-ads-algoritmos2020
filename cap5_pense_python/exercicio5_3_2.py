def gravetos():
    a = float(input('Comprimento de a: ')) //1
    b = float(input('Comprimento de b: ')) //1
    c = float(input('Comprimento de c: ')) //1

    is_triangle(a, b, c)


def is_triangle(a, b, c):
    if a > b+c or b > a+c or c > a+b:
        print('No')
    else:
        print('Yes')


gravetos()