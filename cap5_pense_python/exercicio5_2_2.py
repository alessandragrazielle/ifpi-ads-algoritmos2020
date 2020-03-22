def valores():
    a = float(input('Valor de a: ')) //1
    b = float(input('Valor de b: ')) //1
    c = float(input('Valor de c: ')) //1
    n = float(input('Valor de n: ')) //1

    check_fermat(a, b, c, n)
    

def check_fermat(a, b, c, n):
    if n>2 and a**n + b**n == c**n:
        print('Holy smokes, Fermat was wrong!')
    else:
        print("No, that doesn't work")


valores()