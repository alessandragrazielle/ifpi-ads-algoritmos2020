print('**PROFESSOR 1**')
nome1 = input('Qual seu nome? ')
h1 = int(input('Quantidade de aulas dadas mensalmente: '))
v1 = float(input('Valor da hora aula: '))

print('**PROFESSOR 2**')
nome2 = input('Qual seu nome? ')
h2 = int(input('Quantidade de aulas dadas mensalmente: '))
v2 = float(input('Valor da hora aula: '))


professor1 = h1 * v1
professor2 = h2 * v2


def main():
    print(f'O(A) professor(a) com maior salário é: {salario()}')


def salario():
    if professor1 == professor2:
        return 'Os dois ganham o mesmo valor'
    elif professor1 > professor2:
        return nome1
    else:
        return nome2


main()