li = int(input('Limite Inferior: '))
ls = int(input('Limite Superior: '))


while li <= ls:
    if li > 1:
        if li == 2 or li == 3 or li == 5 or li ==7:
            print(li, end=' ')
        elif li%2 != 0 and li%3 != 0 and li%5 != 0 and li%7 != 0:
            print(li, end=' ')
    li += 1