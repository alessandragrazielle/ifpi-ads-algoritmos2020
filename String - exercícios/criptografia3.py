def main():
    casos = int(input())

    for i in range(casos):
        msg = input()
        
        # passada 1
        def letra_desloca3(msg):
            alfabeto_min = 'abcdefghijklmnopqrstuvwxyz'
            alfabeto_mai = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            msg2 = ''

            for letra in msg:
                if letra in alfabeto_min or letra in alfabeto_mai:
                    posicao = ord(letra)
                    msg2 += chr(posicao + 3)
                else:
                    msg2 += letra

            return msg2


        msg = letra_desloca3(msg)


        # passada 2
        def linha_inverte(msg):
            index = -1
            msg3 = ''

            for letra in msg:
                new_letra = msg[index]
                msg3 += new_letra
                index += -1

            return msg3


        inverso = linha_inverte(msg)


        # passada 3
        def substring(inverso):
            x = len(inverso)
            y = x//2
            metade = ''

            while y < x:
                metade += inverso[y]
                y += 1

            return metade


        metade = substring(inverso)


        def truncada(metade):
            msg5 = ''
            for letra in metade:
                msg5 += chr(ord(letra) - 1)
            
            return msg5


        nova_metade = truncada(metade)


        mensagem_final = inverso.replace(metade, nova_metade)
        print(mensagem_final)



main()