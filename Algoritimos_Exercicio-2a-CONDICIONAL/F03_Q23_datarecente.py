dia_1 = input('Dia 1: ')
mes_1 = input('Mês 1: ')
ano_1 = input('Ano 1: ')

dia_2 = input('Dia 2: ')
mes_2 = input('Mês 2: ')
ano_2 = input('Ano 2: ')



def datas():
    if ano_1 > ano_2:
        print(f'A data mais recente é: {dia_1}/{mes_1}/{ano_1}')


   
    elif ano_1 == ano_2:
        if mes_1 > mes_2:
            print(f'A data mais recente é: {dia_1}/{mes_1}/{ano_1}')
        
        elif mes_1 == mes_2:
            if dia_1 > dia_2:
                print(f'A data mais recente é: {dia_1}/{mes_1}/{ano_1}')
            elif dia_1 == dia_2:
                return 'As datas são iguais'
            else:
                print(f'A data mais recente é: {dia_2}/{mes_2}/{ano_2}')
        
        else:
            print(f'A data mais recente é: {dia_2}/{mes_2}/{ano_2}')

    
    else:
        print(f'A data mais recente é: {dia_2}/{mes_2}/{ano_2}')



datas()
