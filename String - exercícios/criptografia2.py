def main():
    casos = int(input('Quantidade de casos: '))

    for i in range(casos):
        msg = input('Digite a mensagem: ')
        msg2 = ''

        # passo 1
        for letra in msg:
            alfabeto_min = 'abcdefghijklmnopqrstuvwxyz'
            alfabeto_mai = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            
            if letra in alfabeto_min or letra in alfabeto_mai:
                posicao = ord(letra)
                msg2 += chr(posicao + 3)
            else:
                msg2 += letra

        # passo 2
        index = -1
        inverso = ''

        while index >= -len(msg2):
            letter = msg2[index]
            index += -1
            inverso += letter


        # passo 3
        qtd = len(msg)
        metade2 = inverso[qtd//2:]
        msg3 = ''

        for letra2 in metade2:
            msg3 += chr(ord(letra2) - 1)

        mensagem_final = inverso.replace(metade2, msg3)
        print(mensagem_final)

main()
