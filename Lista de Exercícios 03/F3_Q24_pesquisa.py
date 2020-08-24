n = int(input('Número de casos: '))
x = 0
y = 0
z = 0

for a in range(n):
    salario = float(input('Salário: '))
    filhos = int(input('Número de filhos: '))

    soma_s = salario + x
    x = soma_s
    media_s = soma_s/n

    soma_f = filhos + y
    y = soma_f
    media_f = soma_f/n

    if salario <= 1000:
        z += 1

percentual = (z/n)*100

print(f'Média de salário da população: R${media_s:.2f} \nMédia de filhos da população: {media_f:.0f}')
print(f'Percentual de pessoas com salário de até R$1000,00: {percentual:.0f}%')