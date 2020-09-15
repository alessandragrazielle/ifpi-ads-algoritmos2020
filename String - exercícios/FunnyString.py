q = int(input())

for a in range(q):
    s = input()

    # lista 
    letra = 0
    lista = []

    while letra < len(s):
        lista += [ord(s[letra])]
        letra += 1

    # diferenças adjacentes 1
    x = 0
    diferenca = []

    while x < len(lista) - 1:
        diferenca += [abs(lista[x] - lista[x+1])]
        x += 1



    # inverso
    inverso = ''
    index = -1

    while index >= -len(s):
        new_msg = s[index]
        inverso += new_msg
        index += -1


    # lista inverso
    letra_inv = 0
    lista_inv = []

    while letra_inv < len(inverso):
        lista_inv += [ord(inverso[letra_inv])]
        letra_inv += 1

    # diferencas adjacentes 2
    y = 0
    diferenca_inv = []

    while y < len(lista_inv) - 1:
        diferenca_inv += [abs(lista_inv[y] - lista_inv[y+1])]
        y += 1


    # funny or not funny
    if diferenca == diferenca_inv:
        print('Funny')
    else:
        print('Not Funny')