n = int(input('Número: '))
x = 1
y = 0

while x <= n:
    soma = x + y
    y = soma 
    x += 1

media = soma/n

print(f'Soma: {soma} \nMédia: {media}')