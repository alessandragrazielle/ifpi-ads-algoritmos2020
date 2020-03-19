nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))


media = (nota1 + nota2) / 2


def aprovacao():
    if media >= 7:
        print('APROVADO!')
    else :
        exame = float(input('Nota do exame: '))
        media_f = (exame + nota1 + nota2) / 3
        if media_f >= 7:
            print('APROVADO!')
        else:
            print('REPROVADO!')


aprovacao()