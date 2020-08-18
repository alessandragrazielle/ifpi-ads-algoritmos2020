n = int(input('Número: '))
li = int(input('Limite Inferior: '))
ls = int(input('Limite Superior: '))


while li <= ls:
    if li%n == 0:
        print(li, end=' ')
    li += 1