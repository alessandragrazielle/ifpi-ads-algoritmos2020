h = int(input('Quantidades de horas trabalhadas no mês: '))
v = float(input('Valor da hora: '))
salario_bruto = h*v


def main():
    inss = salario_bruto * 10/100
    fgts = salario_bruto * 11/100
    desconto_ir = salario_bruto * ir()/100
    desconto_total = desconto_ir + inss
    salario_liquido = salario_bruto - desconto_total

    print(f'Salário bruto: R${salario_bruto} \n(-)IR ({ir()}%): R${desconto_ir} \n(-)INSS (10%): R${inss}', end='')
    print(f'\nFGTS (11%): R${fgts} \nTotal de descontos: R${desconto_total} \nSalário Líquido: R${salario_liquido}')


def ir():
    if salario_bruto <= 900:
        return 0
    elif salario_bruto <= 1500:
        return 5
    elif salario_bruto <= 2500:
        return 10
    else:
        return 20


main()