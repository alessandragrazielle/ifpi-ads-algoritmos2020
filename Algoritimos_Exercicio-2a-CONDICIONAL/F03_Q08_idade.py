dia_n = int(input('Seu dia de nascimento: '))
mes_n = int(input('Seu mês de nascimento: '))
ano_n = int(input('Seu ano de nascimento: '))

dia_a = int(input('Dia atual: '))
mes_a = int(input('Mês atual: '))
ano_a = int(input('Ano atual: '))


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