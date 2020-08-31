n = int(input('Número: '))
x = 1
y = 0

for a in range (n):
    soma = x + y
    y = soma 
    x += 1

print(f'A soma dos números é: {soma}')