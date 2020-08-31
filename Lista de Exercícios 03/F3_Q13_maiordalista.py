n = int(input('Quantidade de números: '))
x = 1
y = 0

while x <= n:
    num = int(input('Digite um número positivo: '))

    if num > y:
        maior = num

    y = num
    x += 1

print(f'O maior valor é: {maior}')
