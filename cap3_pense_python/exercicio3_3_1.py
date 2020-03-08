# Questão 1
def linha1():
    print('+', 4* ' -', '+', 4* ' -', ' +')


def linha2():
    print (2* '|          ', '|')


def grade():
    for i in range(1):
        linha1()
    for i in range(4):
        linha2()
    for i in range(1):
        linha1()
    for i in range(4):
        linha2()
    for i in range(1):
        linha1()


grade()
