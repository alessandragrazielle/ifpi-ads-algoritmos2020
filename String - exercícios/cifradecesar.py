msg = input('Mensagem: ').lower()
ROT = int(input('Rotação: '))

for letra in msg:
    colocacao = ord(letra)+ROT

    if 97 <= colocacao <= 122:
        print(chr(ord(letra) + ROT), end='')
    elif colocacao < 97:
        x = 97-colocacao
        print(chr(122 - x + 1), end='')
    elif colocacao > 122:
        y = colocacao-122
        print(chr(97 + y - 1), end='')