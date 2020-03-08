def do_twice(f, g):
    f(g)
    f(g)

def print_f(valor):
    print(valor)

do_twice(print_f, 'Alessandra')