li = int(input('Limite Inferior: '))
ls = int(input('Limite Superior: '))


while li <= ls:
    if li%2 == 0:
        print(li, end=' ')
    li += 1