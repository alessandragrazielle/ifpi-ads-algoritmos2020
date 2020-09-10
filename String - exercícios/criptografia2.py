def main():
    casos = int(input('Quantidade de casos: '))

    for i in range(casos):
        msg = input('Digite a mensagem: ')
        msg2 = ''

        # passo 1
        for letra in msg:
            alfabeto_min = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            alfabeto_mai = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            
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