salario = float(input('Qual seu salário? '))

def main():
    vp = salario * tabela_atual() / 100
    vc = salario * tabela_corrigida() / 100

    print(f'Valor pago: R${vp} \nValor que deveria ser pago com a tabela corrigida: R${vc}')


def tabela_atual():
    if salario <= 1903.98:
        return 0
    elif salario <= 2826.65:
        return 7.5
    elif salario <= 3751.05:
        return 15
    elif salario <= 4664.68:
        return 22.5
    else:
        return 27.5


def tabela_corrigida():
    if salario <= 3881.65:
        return 0
    elif salario <= 5714.11:
        return 7.5
    elif salario <= 7654.67:
        return 15
    elif salario <= 9564.42:
        return 22.5
    else:
        return 27.5


main()