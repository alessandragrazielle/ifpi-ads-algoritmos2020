casos = int(input())

for i in range(casos):
    msg = input()
    msg2 = ''

    # passo 1
    for letra in msg:
        if letra.isalpha() == True:
            msg2 += chr(ord(letra) + 3)
        else:
            msg2 += letra

    # passo 2
    msg3 = msg2[::-1]

    # passo 3
    qtd = len(msg)
    x = msg3[qtd//2:]
    msg4 = ''

    for letra2 in x:
        msg4 += chr(ord(letra2) - 1)

    mensagem_final = msg3.replace(x, msg4)
    print(mensagem_final)