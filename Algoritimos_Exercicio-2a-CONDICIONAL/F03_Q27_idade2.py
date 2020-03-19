n = input('Sua data de nascimento: '). split('/')
d = input('Data atual: '). split('/')

dia_n = int(str(n[0]))
mes_n = int(str(n[1]))
ano_n = int(str(n[2]))

dia_a = int(str(d[0]))
mes_a = int(str(d[1]))
ano_a = int(str(d[2]))


def main():
    idade = ano_a - ano_n + anos()
    print(f'Sua idade é de {idade} anos')


def anos():
    if mes_a > mes_n:
        return 0
    elif mes_n >  mes_a:
        return -1
    elif mes_a == mes_n:
        if dia_a >= dia_n:
            return 0
        else:
            return -1


main()