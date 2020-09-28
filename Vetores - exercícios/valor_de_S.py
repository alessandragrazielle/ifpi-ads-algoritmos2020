A = [''] * 20

for i in range(20):
    A[i] = float(input('Digite o valor do elemento: '))

x = 0
y = 19
S = 0
while x<10 and y>9:
    expressao = (A[x] - A[y])**2
    S += expressao

    x += 1
    y -= 1

print(f'O valor de S é: {S}')