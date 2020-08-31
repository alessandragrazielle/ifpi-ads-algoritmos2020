n = int(input('Quantidade de fichas: '))
maior = 1
menor = 1 * 10**20

for a in range(n):
    ni = int(input('Número de identificação: '))
    peso = int(input('Peso: '))
    #nome = input('Nome: ')

    if peso > maior:
        maior = peso
        x = ni
    if peso < menor:
        menor = peso
        y = ni

    

print(f'Boi mais magro: Peso = {menor}kg; Número de identificação = {y} \nBoi mais gordo: Peso = {maior}kg; Número de identificação = {x}')