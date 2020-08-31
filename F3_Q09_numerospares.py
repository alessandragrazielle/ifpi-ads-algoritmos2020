li = int(input('Limite Inferior: '))
ls = int(input('Limite Superior: '))


for a in range(li, ls+1):
    if li%2 == 0:
        print(li, end=' ')
    li += 1