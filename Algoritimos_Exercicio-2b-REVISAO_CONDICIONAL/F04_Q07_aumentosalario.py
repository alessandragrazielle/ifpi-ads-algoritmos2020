salario = float(input('Qual o seu salário? '))


def main():
    novosalario = salario + valoraumento()
    print(f'Salário antes do reajuste: {salario} \nPercentual de aumento aplicado: {percentual()}', end='')  
    print(f'\nValor do aumento: {valoraumento()} \nNovo salário: {novosalario}')


def percentual():
    if salario <= 280:
        return '20%'
    elif 280 < salario <= 700:
        return '15%'
    elif 700 < salario < 1500:
        return '10%'
    else:
        return '5%'


def valoraumento():
    if salario <= 280:
        return salario*20/100
    elif 280 < salario <= 700:
        return salario*15/100
    elif 700 < salario < 1500:
        return salario*10/100
    else:
        return salario*5/100


main()
