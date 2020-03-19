d = input('Digite uma data: '). split('/')

dia = int(str(d[0]))
mes = int(str(d[1]))
ano = int(str(d[2]))


def data():
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia > 31:
            print('A data não é válida')
        else:
            print('A data é válida')
    elif mes == 4 and mes == 6 and mes == 9 and mes == 11:
        if dia > 30:
            print('A data não é válida')
        else:
            print('A data é válida')
    elif mes == 2:
        if dia > 29:
            print('A data não é válida')
        else:
            print('A data é válida')
    elif ano//1000 < 1:
        print('A data não é válida')
    else:
        print('A data não é válida')


data()